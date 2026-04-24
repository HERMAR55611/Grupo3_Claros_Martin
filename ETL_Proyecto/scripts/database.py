import os
from sqlalchemy import create_engine
from urllib.parse import quote_plus

def get_engine():
    try:
        import streamlit as st
        DB_HOST = st.secrets.get("DB_HOST", "")
        DB_PORT = st.secrets.get("DB_PORT", "6543")
        DB_USER = st.secrets.get("DB_USER", "")
        DB_PASSWORD = st.secrets.get("DB_PASSWORD", "")
        DB_NAME = st.secrets.get("DB_NAME", "postgres")
    except:
        DB_HOST = os.getenv("DB_HOST")
        DB_PORT = os.getenv("DB_PORT", "6543")
        DB_USER = os.getenv("DB_USER")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        DB_NAME = os.getenv("DB_NAME", "postgres")

    DATABASE_URL = (
        f"postgresql://{quote_plus(DB_USER)}:{quote_plus(DB_PASSWORD)}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"
    )

    return create_engine(DATABASE_URL)