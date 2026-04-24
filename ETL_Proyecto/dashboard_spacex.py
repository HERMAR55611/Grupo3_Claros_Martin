import streamlit as st
import pandas as pd
from scripts.database import get_engine

st.set_page_config(page_title="Dashboard SpaceX", layout="wide")

st.title("🚀 Dashboard de Lanzamientos SpaceX")

# 🔌 Conexión
engine = get_engine()

# 📥 Cargar datos
query = "SELECT * FROM lanzamientos_spacex"
df = pd.read_sql(query, engine)

# 🧹 Limpieza
df["exito"] = df["exito"].fillna(False)

# 📊 KPIs
total = len(df)
exitos = df["exito"].sum()
fallos = total - exitos

col1, col2, col3 = st.columns(3)

col1.metric("Total lanzamientos", total)
col2.metric("Exitosos", exitos)
col3.metric("Fallidos", fallos)
    
# 📊 Gráfico
st.subheader("📊 Éxitos vs Fallos")
st.bar_chart(df["exito"].value_counts())

# 📅 Mostrar tabla
st.subheader("📋 Datos")
st.dataframe(df)