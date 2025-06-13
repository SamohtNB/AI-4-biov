import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    data_map = pd.DataFrame({
        'lat': [48.8566, 45.7640, 43.6047],  # Paris, Lyon, Toulouse
        'lon': [2.3522, 4.8357, 1.4442]
    })
    return data_map
    

def display():
    
    
    st.title("AI 4 biov")
    st.write("Ceci est la partie frontend du projet")
    st.markdown("""
    ## but du projet
    le but de ce projet est de trouver, grâce à la détection d'images, les décharges sauvages mais aussi de prévoir quelles seront les prochaines décharges sauvages.
    
    ## technologies utilisées
    - Streamlit pour le frontend
    - Yolov5 pour la détection d'images
    - Pandas pour la manipulation des données
    
    ceci est une maquette pour montrer la partie frontend du projet.
    """)
    
    data_map = load_data()
    st.subheader("Carte des décharges sauvages")
    
    st.map(data_map, zoom=5, use_container_width=True)
    
    if st.button("signaler une décharge sauvage"):
        st.file_uploader("Télécharger une image de la décharge sauvage", type=["jpg", "jpeg", "png"])
        st.write("Merci de votre contribution !")

if __name__ == "__main__":
    display()