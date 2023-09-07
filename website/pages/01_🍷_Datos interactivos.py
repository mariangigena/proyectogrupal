import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud
import streamlit as st
from PIL import Image

ruta_reviewfinal = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ReviewFinal.parquet")
df= pd.read_parquet(ruta_reviewfinal)

if st.checkbox("Vista de primeros o últimos datos"):
    if st.button("Primeros Datos"):
        st.write(df.head())
    if st.button("Últimos Datos"):
        st.write(df.tail())

st.write("##### Para poder trabajar con el modelo acordamos que a los nulos en reviews les íbamos a imputar el valor not descripción ya que som los que mas nos afectan.")

st.title('Nube de Palabras de Reseñas')

@st.cache_data
def generate_wordcloud(reviews):
    # Tu código para generar la nube de palabras aquí...
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(reviews)
    return wordcloud

# Obtiene las reseñas y genera la nube de palabras (se ejecutará una vez y se cacheará)
filtered_reviews = df['review'].dropna()
all_reviews = " ".join(str(review) for review in filtered_reviews)
wordcloud = generate_wordcloud(all_reviews)

# Muestra la imagen en Streamlit
st.image(Image.fromarray(np.array(wordcloud)))


#############################################################################################
# Título de la página
st.title('Generador de Nube de Palabras')

# Sidebar para seleccionar el rango de palabras
st.markdown('### Rango de Palabras')
min_words = st.slider('Mínimo', 1, 10, 2)
max_words = st.slider('Máximo', 1, 10, 10)

# Filtra las reseñas por longitud (rango de palabras seleccionado)
filtered_reviews = df[df['review'].apply(lambda x: isinstance(x, str) and min_words <= len(x.split()) <= max_words)]['review']

# Crea un solo string con todas las reseñas filtradas
all_reviews = " ".join(filtered_reviews.astype(str))

# Genera la nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_reviews)
wordcloud_image = Image.fromarray(np.array(wordcloud))

# Mostrar la imagen en Streamlit con el ancho del contenedor
st.image(wordcloud_image, caption='Nube de Palabras', use_column_width=True)

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

######################################################################################
# Título de la página
st.title('Distribución de Calificaciones por Estado')

# Sidebar para seleccionar estados
selected_states = st.multiselect('Selecciona Estados', df['estado'].unique(), default= ['California', 'New_York', 'New_Jersey', 'Ohio'])

# Sidebar para seleccionar puntajes
rating_range = st.slider('Selecciona Rango de Puntajes', 1, 5, (1, 5))

# Filtra los datos según las selecciones de los usuarios
filtered_df = df[df['estado'].isin(selected_states) & (df['rating'] >= rating_range[0]) & (df['rating'] <= rating_range[1])]

# Verifica si el DataFrame filtrado tiene datos
if not filtered_df.empty:
    # Crea la gráfica de distribución de calificaciones
    plt.figure(figsize=(12, 6))
    sns.countplot(data=filtered_df, x='estado', hue='rating', palette='viridis')
    plt.title('Distribución de Calificaciones por Estado')
    plt.xlabel('Estado')
    plt.ylabel('Cantidad de Reseñas')
    plt.legend(title='Rating')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

# Muestra la gráfica en Streamlit
st.pyplot(plt)


##################################################################################################33
