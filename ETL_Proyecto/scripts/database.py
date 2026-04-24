import os
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()

def get_engine():
    # 🔐 Leer credenciales
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    # 🧱 Construir URL de conexión
    DATABASE_URL = (
        f"postgresql://{quote_plus(DB_USER)}:{quote_plus(DB_PASSWORD)}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"
    )

    # ⚙️ Crear engine
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True
    )

    return engine