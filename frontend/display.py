import streamlit as st
import pandas as pd
from signalement import page_signalement
from map_decharge import page_map_decharge

    

def display():
    
    
    st.title("AI 4 biov")
    st.write("Ceci est la partie frontend du projet")
    
    menu = st.selectbox(
        "Choisissez une page",
        ("Accueil", "Signalement de Décharge Sauvage", "Carte des Décharges Sauvages")
    )
    
    if menu == "Accueil":
        st.markdown("""
        ## but du projet
        le but de ce projet est de trouver, grâce à la détection d'images, les décharges sauvages mais aussi de prévoir quelles seront les prochaines décharges sauvages.
        
        ## technologies utilisées
        - Streamlit pour le frontend
        - Yolov5 pour la détection d'images
        - Pandas pour la manipulation des données
        
        ceci est une maquette pour montrer la partie frontend du projet.
        """)
    
    elif menu == "Carte des Décharges Sauvages":
        page_signalement()

    elif menu == "Signalement de Décharge Sauvage":
        page_map_decharge()

if __name__ == "__main__":
    display()