import streamlit as st
import pandas as pd

st.set_page_config(page_title="Carte des Décharges Sauvages", layout="wide")

@st.cache_data
def load_data():
    data_map = pd.DataFrame({
        'lat': [48.8566, 45.7640, 43.6047],  # Paris, Lyon, Toulouse
        'lon': [2.3522, 4.8357, 1.4442]
    })
    return data_map

def page_map_decharge():
    data_map = load_data()
    st.subheader("Carte des décharges sauvages")
    
    st.map(data_map, zoom=5, use_container_width=True)