import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Configuración de la página (DEBE ser el primer comando de Streamlit)
st.set_page_config(page_title="Analizador de Sentimientos", page_icon="😊")

# Descargar recursos necesarios de NLTK
@st.cache_resource
def download_nltk_resources():
    nltk.download('vader_lexicon')

download_nltk_resources()

st.title("Analizador de Sentimientos")
st.write("Esta aplicación analiza el sentimiento de un texto utilizando VADER.")

# Entrada de texto
text_input = st.text_area("Ingresa el texto a analizar:", height=150)

# Análisis de sentimiento
if st.button("Analizar"):
    if text_input:
        # Inicializar el analizador
        sid = SentimentIntensityAnalyzer()
        
        # Obtener puntuaciones de sentimiento
        sentiment_scores = sid.polarity_scores(text_input)
        
        # Mostrar resultados
        st.write("### Resultados del análisis")
        
        # Crear un DataFrame para visualización
        scores_df = pd.DataFrame({
            'Categoría': ['Negativo', 'Neutral', 'Positivo', 'Compuesto'],
            'Puntuación': [
                sentiment_scores['neg'], 
                sentiment_scores['neu'], 
                sentiment_scores['pos'], 
                sentiment_scores['compound']
            ]
        })
        
        # Mostrar tabla de puntuaciones
        st.dataframe(scores_df)
        
        # Visualización
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = sns.barplot(x='Categoría', y='Puntuación', data=scores_df.iloc[:3], ax=ax)
        
        # Colorear las barras según el sentimiento
        colors = ['#ff9999', '#cccccc', '#99ff99']
        for i, bar in enumerate(bars.patches):
            bar.set_color(colors[i])
            
        plt.title('Análisis de Sentimiento')
        st.pyplot(fig)
        
        # Interpretación del resultado
        compound = sentiment_scores['compound']
        if compound >= 0.05:
            st.success(f"El texto tiene un sentimiento POSITIVO (puntuación: {compound:.2f})")
        elif compound <= -0.05:
            st.error(f"El texto tiene un sentimiento NEGATIVO (puntuación: {compound:.2f})")
        else:
            st.info(f"El texto tiene un sentimiento NEUTRAL (puntuación: {compound:.2f})")
    else:
        st.warning("Por favor, ingresa un texto para analizar.")

# Información adicional
with st.expander("¿Cómo funciona?"):
    st.write("""
    Este analizador utiliza VADER (Valence Aware Dictionary and sEntiment Reasoner), 
    que es una herramienta de análisis de sentimientos basada en reglas y léxico.
    
    - **Puntuación negativa**: Proporción del texto que es negativa
    - **Puntuación neutral**: Proporción del texto que es neutral
    - **Puntuación positiva**: Proporción del texto que es positiva
    - **Puntuación compuesta**: Valor normalizado entre -1 (muy negativo) y +1 (muy positivo)
    """)