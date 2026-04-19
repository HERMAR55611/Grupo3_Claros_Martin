import os

def get_db_config():
    # Intento 1: Streamlit Cloud
    try:
        import streamlit as st
        host = st.secrets.get("DB_HOST", "")
        if host and host != "localhost":
            return {
                "host": host,
                "port": st.secrets.get("DB_PORT", "5432"),
                "user": st.secrets.get("DB_USER", "postgres"),
                "password": st.secrets.get("DB_PASSWORD", ""),
                "dbname": st.secrets.get("DB_NAME", "postgres"),
            }
    except Exception:
        pass

    # Intento 2: .env local
    return {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": os.getenv("DB_PORT", "5432"),
        "user": os.getenv("DB_USER", "postgres"),
        "password": os.getenv("DB_PASSWORD", ""),
        "dbname": os.getenv("DB_NAME", "postgres"),
    }