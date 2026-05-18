import requests
import pandas as pd
import logging
from sqlalchemy import text
from scripts.database import get_connection

logging.basicConfig(level=logging.INFO)

BASE_URL = "https://api.spacexdata.com/v4/launches"

def extraer_lanzamientos():
    try:
        logging.info("🚀 Extrayendo lanzamientos de SpaceX...")

        response = requests.get(BASE_URL)
        response.raise_for_status()

        data = response.json()

        lanzamientos = []

        for lanzamiento in data:
            lanzamientos.append({
                "nombre": lanzamiento.get("name"),
                "fecha": lanzamiento.get("date_utc"),
                "exito": lanzamiento.get("success"),
                "cohete_id": lanzamiento.get("rocket"),
                "detalles": lanzamiento.get("details")
            })

        df = pd.DataFrame(lanzamientos)

        conn = get_connection()

        logging.info("📦 Insertando datos en Supabase...")

        query = text("""
        INSERT INTO lanzamientos_spacex 
        (nombre, fecha, exito, cohete_id, detalles)
        VALUES (:nombre, :fecha, :exito, :cohete_id, :detalles)
        """)

        registros = df.to_dict(orient="records")

        conn.execute(query, registros)
        conn.commit()
        conn.close()

        logging.info(f"✅ {len(df)} registros insertados en Supabase")

    except Exception as e:
        logging.error(f"❌ Error: {e}")

if __name__ == "__main__":
    extraer_lanzamientos()