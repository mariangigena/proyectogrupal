import streamlit as st
import os


st.set_page_config(
    page_title= "Review Insights - Bienvenidos",
    page_icon= "Images/handshake-regular.svg",
    layout= "wide",
    initial_sidebar_state= "auto"
)

image_path = os.path.join(os.path.dirname(__file__), "Banner.png")
st.image(image_path, use_column_width= True)


st.title("Review Insights - Análisis de Reseñas y Recomendaciones")
st.markdown('***')

st.sidebar.markdown('### Menu Interactivo')

# Introducción
st.header('Introducción')
st.write("Review Insights es una empresa de análisis de datos que tiene como objetivo proporcionar información valiosa a otras empresas sobre las reseñas y recomendaciones que reciben de los usuarios en plataformas como Yelp y Google Maps. Nuestro enfoque principal es recopilar, analizar y ofrecer información significativa sobre las experiencias de los usuarios en diferentes comercios.")

# Contexto
st.header('Contexto')
st.write("La industria vinícola se destaca por su enfoque único en la valoración de la marca a través de opiniones personales y recomendaciones de expertos en guías especializadas...")

