import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = conn.cursor()

df = pd.read_csv("data_transformada.csv")

for _, row in df.iterrows():
    # Insertar ciudad (si no existe)
    cursor.execute(
        "INSERT INTO ciudades (nombre, pais) VALUES (%s, %s) ON CONFLICT (nombre) DO NOTHING;",
        (row["ciudad"], "Colombia")
    )

    # Obtener id de ciudad
    cursor.execute(
        "SELECT id FROM ciudades WHERE nombre = %s;",
        (row["ciudad"],)
    )
    ciudad_id = cursor.fetchone()[0]

    # Insertar registro clima
    cursor.execute(
        """
        INSERT INTO registros_clima (
            ciudad_id, temperatura, humedad, velocidad_viento, descripcion
        ) VALUES (%s, %s, %s, %s, %s);
        """,
        (
            ciudad_id,
            row["temperatura"],
            row["humedad"],
            row["velocidad_viento"],
            row["descripcion"]
        )
    )

conn.commit()
cursor.close()
conn.close()

print("✅ 1000 registros cargados en Supabase")