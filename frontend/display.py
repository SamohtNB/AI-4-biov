import streamlit as st
import pandas as pd
from signalement import page_signalement
from map_decharge import page_map_decharge

st.set_page_config(page_title="AI 4 biov", layout="wide")

def page_accueil():
    st.title("AI 4 biov")
    st.write("Ceci est la partie frontend du projet")
    
    st.sidebar.title("Navigation")
    
    menu = st.sidebar.radio("Choisissez une page",
            ["Accueil", "Carte des Décharges Sauvages", "Signalement de Décharge Sauvage"])
    
    if menu == "Accueil":
        st.markdown("""
        ## but du projet
        le but de ce projet est de trouver, grâce à la détection d'images, les décharges sauvages mais aussi de prévoir quelles seront les prochaines décharges sauvages.
        
        ## technologies utilisées
        - Streamlit pour le frontend
        - Yolov5 pour la détection d'images
        - Pandas pour la manipulation des données
        
        ceci est une maquette pour montrer la partie frontend du projet.
        
        sur le côté gauche, vous pouvez naviguer entre les différentes pages du projet.
        """)
    
    elif menu == "Carte des Décharges Sauvages":
        page_signalement()

    elif menu == "Signalement de Décharge Sauvage":
        page_map_decharge()

if __name__ == "__main__":
    page_accueil()