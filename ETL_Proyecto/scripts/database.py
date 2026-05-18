import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    if not all([DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME]):
        raise ValueError("❌ Faltan variables en .env")

    DATABASE_URL = (
        f"postgresql://{quote_plus(DB_USER)}:{quote_plus(DB_PASSWORD)}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    return create_engine(DATABASE_URL)