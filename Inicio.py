import streamlit as st
import base64

# Convertir imagen a base64
def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Crear el CSS con la imagen base64
def set_background(picture_file):
    bin_str = get_base64(picture_file)
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bin_str}");
        background-size: cover;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Usar el fondo
set_background("fondo.jpg")

# Titulo
st.title("¡Bienvenido a la experiencia Sommelier!")

st.write("Selecciona una opcion desde el menú lateral.")



# https://docs.streamlit.io/library/get-started/multipage-apps
# Local: streamlit run streamlit_tutorial.py
# Streamlit Sharing 
# render, heroku, AWS EC2