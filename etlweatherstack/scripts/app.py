import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título
st.title("🚀 Análisis de Lanzamientos SpaceX")

# Cargar datos
df = pd.read_csv('data/spacex.csv')

st.subheader("📊 Datos de lanzamientos")
st.dataframe(df)

st.subheader("🚀 Tasa de éxito")

tasa = df['exito'].mean() * 100
st.metric("Éxito (%)", f"{tasa:.2f}%")

import matplotlib.pyplot as plt

conteo = df['exito'].value_counts()

fig, ax = plt.subplots()
conteo.plot(kind='bar', ax=ax)
ax.set_title("Lanzamientos exitosos vs fallidos")
ax.set_xticklabels(['Fallido', 'Exitoso'], rotation=0)

st.pyplot(fig)

st.title("🚀 Dashboard SpaceX")
st.write("Análisis de lanzamientos")

# Procesamiento
df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
df['año'] = df['fecha'].dt.year
df['exito'] = df['exito'].apply(lambda x: 1 if x == True else 0)

# Mostrar datos
st.subheader("📄 Datos")
st.dataframe(df.head())

# Gráfico lanzamientos por año
st.subheader("📊 Lanzamientos por año")
lanzamientos = df['año'].value_counts().sort_index()

fig, ax = plt.subplots()
lanzamientos.plot(kind='bar', ax=ax)
st.pyplot(fig)

# Éxito vs fracaso
st.subheader("🎯 Éxito vs Fallo")
exito = df['exito'].value_counts()

fig2, ax2 = plt.subplots()
exito.plot(kind='pie', autopct='%1.1f%%', ax=ax2)
st.pyplot(fig2)