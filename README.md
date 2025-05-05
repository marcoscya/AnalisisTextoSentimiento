# Herramienta de Análisis de Sentimientos - Analizar el sentimiento de texto

Esta aplicación web permite analizar el sentimiento de textos utilizando técnicas de procesamiento de lenguaje natural. La herramienta clasifica los textos como positivos, negativos o neutros basándose en su contenido emocional.

## Características

- Análisis de sentimiento en tiempo real
- Visualización gráfica de los resultados
- Puntuaciones detalladas para sentimientos positivos, negativos y neutros
- Interfaz intuitiva desarrollada con Streamlit

## Tecnologías utilizadas

- Python
- Streamlit para la interfaz de usuario
- NLTK (Natural Language Toolkit) con VADER para el análisis de sentimientos
- Pandas para el manejo de datos
- Matplotlib y Seaborn para visualizaciones

## Limitaciones

Es importante destacar que esta herramienta utiliza VADER (`nltk.sentiment.vader.SentimentIntensityAnalyzer`), que está diseñada principalmente para textos en inglés. Por esta razón, algunas palabras en español con carga emocional fuerte (como "odio", "amor", etc.) pueden ser clasificadas incorrectamente como neutras.

El léxico de VADER se encuentra en el [repositorio oficial de VADER](https://github.com/cjhutto/vaderSentiment), donde se pueden consultar las palabras clave y sus valores de sentimiento asociados.

## Visualizacion (Sentimiento Positivo)
![image](https://github.com/user-attachments/assets/2ec5701f-e9d0-477f-9a68-7ac789288575)
![image](https://github.com/user-attachments/assets/333045b9-05f7-40f4-bf9d-a065866e969a)
![image](https://github.com/user-attachments/assets/5c2d2d18-8d7a-44cb-a495-2d52bd740463)

### Sentimiento Negativo
![image](https://github.com/user-attachments/assets/af3dc6eb-05c6-4111-a387-abdd494e5cc8)
![image](https://github.com/user-attachments/assets/4008dd98-d384-4217-8023-47473cef9c73)

### Sentimiento Neutral
![image](https://github.com/user-attachments/assets/efc9147d-c340-4be9-b5cb-3a4b1abe13b4)
![image](https://github.com/user-attachments/assets/221d5261-e30d-48cc-9e0c-ff11ebf0995d)





## 🚀 Instalación y ejecución

```bash
# 1. Crear entorno virtual
python -m venv venv

# 2. Activar entorno virtual (Windows)
venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. (Opcional) Actualizar requirements.txt con las versiones exactas
pip freeze > requirements.txt

# 5. Ejecutar la aplicación con Streamlit
streamlit run app.py
