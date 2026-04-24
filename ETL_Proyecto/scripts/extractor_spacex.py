import requests
import pandas as pd
import os
import logging

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

        os.makedirs("data", exist_ok=True)
        df.to_csv("data/lanzamientos_spacex.csv", index=False)

        logging.info("✅ Datos guardados en data/lanzamientos_spacex.csv")

    except Exception as e:
        logging.error(f"❌ Error: {e}")

if __name__ == "__main__":
    extraer_lanzamientos()
