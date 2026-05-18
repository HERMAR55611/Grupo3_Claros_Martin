import pandas as pd
import matplotlib.pyplot as plt
import logging

logging.basicConfig(level=logging.INFO)

def visualizar():
    try:
        logging.info("📊 Cargando datos...")

        df = pd.read_csv("data/lanzamientos_spacex.csv")

        # Reemplazar valores nulos en exito
        df["exito"] = df["exito"].fillna(False)

        # Conteo de éxitos vs fallos
        conteo = df["exito"].value_counts()

        plt.figure()
        conteo.plot(kind="bar")

        plt.title("Lanzamientos Exitosos vs Fallidos - SpaceX")
        plt.xlabel("Éxito")
        plt.ylabel("Cantidad")

        plt.tight_layout()
        plt.savefig("data/analisis_spacex.png")

        logging.info("✅ Gráfico guardado en data/analisis_spacex.png")

    except Exception as e:
        logging.error(f"❌ Error en visualización: {e}")

if __name__ == "__main__":
    visualizar()
