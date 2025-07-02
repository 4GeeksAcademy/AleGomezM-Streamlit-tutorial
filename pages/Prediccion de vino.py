import streamlit as st
import numpy as np
import joblib

# Cargar modelo y scaler
modelo = joblib.load('modelo.pkl')
scaler = joblib.load('scaler.pkl')

# Título de la aplicación
st.title("Predicción de Calidad del Vino 🍷")
st.image('calidad vino.jpg', width=550, use_container_width=False)
st.write("Introduce las características del vino:")

# Entradas del usuario
def entrada_caracteristicas():
    fixed_acidity = st.number_input("Fixed Acidity", 0.0, 20.0, 7.0)
    volatile_acidity = st.number_input("Volatile Acidity", 0.0, 2.0, 0.7)
    citric_acid = st.number_input("Citric Acid", 0.0, 1.0, 0.0)
    residual_sugar = st.number_input("Residual Sugar", 0.0, 15.0, 1.9)
    chlorides = st.number_input("Chlorides", 0.0, 1.0, 0.076)
    free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", 0.0, 100.0, 11.0)
    total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", 0.0, 300.0, 34.0)
    density = st.number_input("Density", 0.9900, 1.0050, 0.9978)
    ph = st.number_input("pH", 2.5, 4.5, 3.51)
    sulphates = st.number_input("Sulphates", 0.0, 2.0, 0.56)
    alcohol = st.number_input("Alcohol", 5.0, 15.0, 9.4)

    return np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                      chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
                      ph, sulphates, alcohol]])

input_data = entrada_caracteristicas()

if st.button("Predecir Calidad"):
    input_scaled = scaler.transform(input_data)
    prediccion = modelo.predict(input_scaled)[0]
    st.success(f"La calidad del vino se predice como: **{prediccion.upper()}** ")