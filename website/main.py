import streamlit as st
import os


st.set_page_config(
    page_title= "Review Insights - Bienvenidos",
    page_icon= "🍷",
    layout= "wide",
    initial_sidebar_state= "auto"
)

image_path = os.path.join(os.path.dirname(__file__), "Banner.png")
st.image(image_path, use_column_width= True)


st.title("Review Insights - Análisis de Reseñas y Recomendaciones")
st.markdown('***')

# Enlace al video de YouTube
video_url = "https://www.youtube.com/watch?v=lvNvFnLGZss"

# Muestra el enlace como texto enriquecido
st.video(video_url)

st.sidebar.markdown('### Menu Interactivo')


# Introducción
st.header('Introducción')
st.write("`Review Insights` es una empresa de análisis de datos que tiene como objetivo proporcionar información valiosa a otras empresas sobre las reseñas y recomendaciones que reciben de los usuarios en plataformas como Yelp y Google Maps. Nuestro enfoque principal es recopilar, analizar y ofrecer información significativa sobre las experiencias de los usuarios en diferentes comercios.")

# Contexto
st.header('Contexto')
st.write("La industria vinícola se destaca por su enfoque único en la valoración de la marca a través de opiniones personales y recomendaciones de expertos en guías especializadas, así como del poderoso efecto del boca a boca entre los consumidores. Estados Unidos, conocido tradicionalmente por su cultura cervecera, ha experimentado un crecimiento constante en el consumo de vino en los últimos años. Esta tendencia positiva representa una oportunidad valiosa para comercializar productos vinícolas en el país. La capacidad de identificar y clasificar a los `reviewers` en profesionales o consumidores circunstanciales, junto con el análisis comparativo de las calificaciones otorgadas por ambos grupos, permitirá a las empresas entender mejor el impacto de las opiniones expertas y del público general en la percepción y éxito de sus establecimientos. Adicionalmente, la estimación realizada por estudios de marketing, sobre el aumento del consumo de vino en los años venideros fortalece aún más la relevancia del proyecto. La información proporcionada por esta plataforma será invaluable para las empresas vinícolas en sus esfuerzos de marketing, toma de decisiones estratégicas y mejora continua de la calidad del servicio.")