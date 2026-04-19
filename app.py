import streamlit as st
import psycopg2

st.title("Dashboard Clima 🌦️")

try:
    conn = psycopg2.connect(
        host=st.secrets["DB_HOST"],
        port=st.secrets["DB_PORT"],
        database=st.secrets["DB_NAME"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASSWORD"]
    )

    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM ciudades;")
    ciudades = cursor.fetchall()

    st.success("✅ Conexión exitosa")

    st.write("Ciudades registradas:")
    st.write(ciudades)

except Exception as e:
    st.error(f"❌ Error: {e}")