import streamlit as st

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
    
    st.map