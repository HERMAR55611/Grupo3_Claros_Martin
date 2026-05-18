import requests
import pandas as pd

# URL de SpaceX
url = "https://api.spacexdata.com/v4/launches"

# Petición
response = requests.get(url)

# Verificar respuesta
if response.status_code == 200:
    data = response.json()
    print("✅ API conectada")
else:
    print("❌ Error en API")
    exit()

# Convertir a DataFrame
df = pd.DataFrame(data)

# Seleccionar columnas
df = df[['name', 'date_utc', 'success']]

# Renombrar
df.columns = ['mision', 'fecha', 'exito']

# Guardar CSV
df.to_csv("data/spacex.csv", index=False)

print("✅ Archivo spacex.csv creado")