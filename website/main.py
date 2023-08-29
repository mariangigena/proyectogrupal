import streamlit as st
from PIL import Image 

st.set_page_config(
    page_title= "Review Insights - Bienvenidos",
    page_icon= "./Images/handshake-regular.svg",
    layout= "wide",
    initial_sidebar_state= "auto"
)

# background = Image.open('./Images/Background.png')
# st.image(background, use_column_width= True)

logo = Image.open('./Images/Banner.png')
st.image(logo, use_column_width= True)

# Cargar el CSS personalizado
# st.markdown('<style>' + open('styles.css').read() + '</style>', unsafe_allow_html=True)


st.title("Bienvenidos a Review Insights")

st.markdown('***')
st.markdown("## ¿Te deployamos la vida?")

st.sidebar.markdown('### Menu Interactivo')
