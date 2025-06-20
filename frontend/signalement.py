import streamlit as st

st.set_page_config(page_title="Signalement de Décharge Sauvage", layout="wide")

def page_signalement():
    st.title("Signaler une Décharge Sauvage")
    st.write("Merci de contribuer à la protection de l'environnement en signalant les décharges sauvages.")

    file_public_waste = st.file_uploader("Télécharger une image de la décharge sauvage", type=["jpg", "jpeg", "png"])
    st.write("pourriez vous préciser l'emplacement de la décharge sauvage ?(latitude, longitude)")
    location = st.text_input("Emplacement (latitude, longitude)", placeholder="Ex: 48.8566, 2.3522")
    
    if file_public_waste is not None and st.button("Envoyer le signalement"):
        st.image(file_public_waste, caption="Image téléchargée", use_column_width=True)
        st.success(f"Signalement envoyé avec succès !\nEmplacement: {location}")
    else:
        st.warning("Veuillez télécharger une image pour signaler une décharge sauvage.")
        

if __name__ == "__main__":
    page_signalement()