import streamlit as st
import pandas as pd
import pickle
import numpy as np
import os


# Título de la aplicación
st.title("🍷 Predicción de Calidad del Vino")
st.image('calidad vino.jpg', width=550, use_column_width=False)



def load_model():
    # Obtener la raíz del repositorio (subir un nivel desde 'pages')
    base_dir = os.path.dirname(os.path.dirname(__file__)) if "__file__" in globals() else os.getcwd()
    model_path = os.path.join(base_dir, "models", "knn_wine_model.pkl")
    model_path = os.path.abspath(model_path)  # para debug y seguridad
    st.text(f"Cargando modelo desde: {model_path}")
    
    if not os.path.exists(model_path):
        st.error(f"El archivo {model_path} no existe.")
        return None
    
    try:
        with open(model_path, "rb") as f:
            modelo_knn = pickle.load(f)
        return modelo_knn
    except Exception as e:
        st.error(f"Error al cargar el modelo: {str(e)}")
        return None

#@st.cache_resource
#def load_scaler():
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    return scaler

modelo_knn = load_model()
#escalador = load_scaler()

# Nombres de las características
feature_names = [
    "Fixed Acidity",
    "Volatile Acidity",
    "Citric Acid",
    "Residual Sugar",
    "Chlorides",
    "Free Sulfur Dioxide",
    "Total Sulfur Dioxide",
    "Density",
    "pH",
    "Sulphates",
    "Alcohol"
]

st.write("Introduce las características químicas del vino para predecir su calidad:")

# Crear inputs para cada característica
user_inputs = []
for feature in feature_names:
    value = st.number_input(f"{feature}:", min_value=0.0, max_value=100.0, step=0.1)
    user_inputs.append(value)

# Botón para predecir
if st.button("Predecir Calidad"):
    if len(user_inputs) == 11:
        # Convertir a DataFrame
        features_df = pd.DataFrame([user_inputs], columns=feature_names)

        # Escalar
        features_scaled = escalador.transform(features_df)

        # Predecir
        pred = modelo_knn.predict(features_scaled)[0]
        calidad_map = {
            0: "baja 😣",
            1: "media 😄",
            2: "alta 😎"
        }
        calidad = calidad_map.get(pred, "desconocida ❓")

        st.success(f"🔍 Resultado: Este vino probablemente sea de calidad **{calidad}** 🍷")
    else:
        st.error("Debe completar todas las características.")


