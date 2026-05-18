import streamlit as st
import pandas as pd
from scripts.database import get_engine

st.set_page_config(page_title="SpaceX Dashboard", layout="wide")

st.title("🚀 Dashboard de Lanzamientos SpaceX")

# 🔌 Conexión
engine = get_engine()

# 📥 Datos
df = pd.read_sql("SELECT * FROM lanzamientos_spacex", engine)

# 🧹 Limpieza
df["fecha"] = pd.to_datetime(df["fecha"])
df["exito"] = df["exito"].fillna(False)

# 🎯 KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total lanzamientos", len(df))
col2.metric("Exitosos", df["exito"].sum())
col3.metric("Fallidos", len(df) - df["exito"].sum())

st.divider()

# 📊 Gráfico 1: Éxito vs fallo
st.subheader("📊 Lanzamientos exitosos vs fallidos")
conteo = df["exito"].value_counts()
st.bar_chart(conteo)

# 📈 Gráfico 2: Lanzamientos por año
st.subheader("📅 Lanzamientos por año")
df["año"] = df["fecha"].dt.year
lanzamientos_por_año = df["año"].value_counts().sort_index()
st.line_chart(lanzamientos_por_año)

# 🔎 Filtro
st.subheader("🔍 Filtrar por éxito")

filtro = st.selectbox("Selecciona tipo:", ["Todos", "Exitosos", "Fallidos"])

if filtro == "Exitosos":
    df = df[df["exito"] == True]
elif filtro == "Fallidos":
    df = df[df["exito"] == False]

st.dataframe(df)