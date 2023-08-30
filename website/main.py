import streamlit as st
# from PIL import Image 

st.set_page_config(
    page_title= "Review Insights - Bienvenidos",
    page_icon= "Images/handshake-regular.svg",
    layout= "wide",
    initial_sidebar_state= "auto"
)

# background = Image.open('./Images/Background.png')
# st.image(background, use_column_width= True)

# logo = st.image('./Images/Banner.png', caption= 'Banner')
st.image('./Images/Banner.png', use_column_width= True)

# Cargar el CSS personalizado
# st.markdown('<style>' + open('styles.css').read() + '</style>', unsafe_allow_html=True)


st.title("Review Insights - Análisis de Reseñas y Recomendaciones")
st.markdown('***')

st.sidebar.markdown('### Menu Interactivo')

# Introducción
st.header('Introducción')
st.write("Review Insights es una empresa de análisis de datos que tiene como objetivo proporcionar información valiosa a otras empresas sobre las reseñas y recomendaciones que reciben de los usuarios en plataformas como Yelp y Google Maps. Nuestro enfoque principal es recopilar, analizar y ofrecer información significativa sobre las experiencias de los usuarios en diferentes comercios.")

# Contexto
st.header('Contexto')
st.write("La industria vinícola se destaca por su enfoque único en la valoración de la marca a través de opiniones personales y recomendaciones de expertos en guías especializadas...")

