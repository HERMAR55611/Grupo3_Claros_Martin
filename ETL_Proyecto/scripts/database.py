import streamlit as st
from urllib.parse import quote_plus
from sqlalchemy import create_engine

def get_engine():
    DB_HOST = st.secrets.get("DB_HOST")
    DB_PORT = st.secrets.get("DB_PORT")
    DB_USER = st.secrets.get("DB_USER")
    DB_PASSWORD = st.secrets.get("DB_PASSWORD")
    DB_NAME = st.secrets.get("DB_NAME")

    if not all([DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME]):
        raise ValueError("❌ Faltan variables en st.secrets")

    DATABASE_URL = (
        f"postgresql://{quote_plus(DB_USER)}:{quote_plus(DB_PASSWORD)}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"
    )

    return create_engine(DATABASE_URL)