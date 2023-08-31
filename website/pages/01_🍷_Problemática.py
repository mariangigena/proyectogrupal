import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Problemática
st.header('Problemática')
st.write("En el contexto de la industria vinícola en Estados Unidos, las empresas enfrentan el desafío de evaluar la percepción y opinión de los usuarios sobre sus bodegas y bares o clubes de vinos...")


if st.checkbox("Saludo"):
    st.write("Hola")

# Definimos las columnas que nos interesan
fields = ['country', 'points','price', 'variety']

# Cargamos el DataFrame solo con esas columnas
ruta_archivo = os.path.join(os.path.dirname(os.path.dirname(__file__)), "wine_reviews.csv")
wine_reviews = pd.read_csv(ruta_archivo, usecols = fields)
wine_reviews.dropna(inplace = True)

if st.checkbox("Mostrar Tabla de datos"):
    st.dataframe(wine_reviews)

if st.checkbox("Vista de primeros o últimos datos"):
    if st.button("Primeros Datos"):
        st.write(wine_reviews.head())
    if st.button("Últimos Datos"):
        st.write(wine_reviews.tail())

col_row_option = st.radio("Elija la opción de visualización: ", ('Filas', 'Columnas'), horizontal= True)
if col_row_option == 'Filas':
    st.write(wine_reviews.shape[0])
if col_row_option == 'Columnas':
    st.write(wine_reviews.shape[1])

precio_limite = st.slider("Definir Precio Máximo", 0, 4000, 250)

fig = plt.figure(figsize= (6,4))
sns.scatterplot(x= 'price', y= 'points', data= wine_reviews[wine_reviews['price'] < precio_limite])
st.pyplot(fig)

lista_country = wine_reviews['country'].unique().tolist()
countries = st.multiselect("Seleccione los países a Analizar", lista_country, default= ['Argentina', 'Chile', 'Spain'])

fig = plt.figure(figsize= (6,4))
sns.scatterplot(x= 'price', y= 'points', hue= 'country', data= wine_reviews[wine_reviews['country'].isin(countries)])
st.pyplot(fig)