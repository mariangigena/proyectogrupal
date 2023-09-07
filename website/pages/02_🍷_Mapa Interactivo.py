import streamlit as st
import pandas as pd
import pydeck as pdk
import os
from urllib.error import URLError

# Alcances y Objetivos
st.header('Mapa Interactivo de Estados Unidos')
st.write("Este mapa permite ver la ubicación y nombres de lugares de acuerdo a la categoría seleccionada en el menu lateral")


# Obtener la ruta al directorio que contiene tu página de Streamlit
current_directory = os.path.dirname(__file__)

# Definir una función para cargar los datos desde archivos .parquet
@st.cache_data
def load_parquet_data(filename):
    filepath = os.path.join(current_directory, "..", filename)  # Subir un nivel para acceder a los archivos .parquet
    data = pd.read_parquet(filepath)
    return data

# Lista de archivos .parquet que deseas cargar
parquet_files = [
    {"name": "Wine Bar", "file": "map_bar.parquet"},
    {"name": "Winery, Tourist attraction", "file": "map_tourist.parquet"},
    {"name": "Winery, Tourist attraction, Vineyard", "file": "map_vineyard.parquet"},
    {"name": "Winery", "file": "map_winery.parquet"},
    {"name": "Wine Store", "file": "map_wine_store.parquet"}
]

# Barra lateral para seleccionar las capas utilizando casillas de verificación
selected_layers = st.sidebar.multiselect("Select Layers", [layer_info["name"] for layer_info in parquet_files], default=[layer_info["name"] for layer_info in parquet_files])

# Crear una lista de capas ScatterplotLayer a partir de las capas seleccionadas
layers = []
show_names = st.sidebar.checkbox("Show Names", True)  # Casilla de verificación para activar/desactivar los nombres

for layer_info in parquet_files:
    if layer_info["name"] in selected_layers:
        data = load_parquet_data(layer_info["file"])
    
        scatterplot_layer = pdk.Layer(
            "ScatterplotLayer",
            data=data,
            get_position=["longitude", "latitude"],
            get_radius=200,  # Tamaño de los marcadores
            get_fill_color=[200, 30, 0, 160],  # Color de los marcadores
            pickable=True,
            auto_highlight=True,
            id=layer_info["name"]  # Usar el nombre personalizado como ID
        )
    
        # Capa TextLayer para mostrar los nombres si está activada
        if show_names:
            text_layer = pdk.Layer(
                "TextLayer",
                data=data,
                get_position=["longitude", "latitude"],
                get_text="name_y",  # El nombre de la columna que contiene los nombres
                get_color=[255, 255, 0, 200],  # Amarillo brillante (RGBA)
                get_size=14,
                get_alignment_baseline="'bottom'",
            )
            layers.append(text_layer)  # Agregar la capa de nombres si está activada
    
        layers.append(scatterplot_layer)  # Agregar la capa de puntos

# Configurar la vista inicial del mapa
view_state = pdk.ViewState(
    latitude=37.76,
    longitude=-122.4,
    zoom=11,
    pitch=50
)

# Crear el mapa con las capas seleccionadas
if layers:
    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=view_state,
        layers=layers
    ))
else:
    st.warning("Please select at least one layer to display.")
