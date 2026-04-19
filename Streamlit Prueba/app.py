import streamlit as st
import requests
import pandas as pd

# TU API KEY
API_KEY = "7c3a05da17684a477e4da48747138143"

ciudades = ["Bogota","Medellin","Cali","Barranquilla","Cartagena"]

st.title("🌦️ Dashboard del Clima")

datos = []

for ciudad in ciudades:

    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={ciudad}"
    response = requests.get(url)
    data = response.json()

    if "current" in data:

        datos.append({
            "Ciudad": ciudad,
            "Temperatura": data["current"]["temperature"],
            "Humedad": data["current"]["humidity"],
            "Viento": data["current"]["wind_speed"],
            "Descripción": data["current"]["weather_descriptions"][0]
        })

df = pd.DataFrame(datos)

st.subheader("📊 Datos actuales del clima")
st.dataframe(df)

st.subheader("🌡️ Temperatura por ciudad")
st.bar_chart(df.set_index("Ciudad")["Temperatura"])

st.subheader("💧 Humedad por ciudad")
st.bar_chart(df.set_index("Ciudad")["Humedad"])