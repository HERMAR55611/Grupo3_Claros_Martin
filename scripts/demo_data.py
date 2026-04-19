import random
import pandas as pd

ciudades = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena"]

data = []

for _ in range(1000):
    ciudad = random.choice(ciudades)
    data.append({
        "ciudad": ciudad,
        "temperatura": round(random.uniform(15, 35), 2),
        "humedad": round(random.uniform(40, 90), 2),
        "velocidad_viento": round(random.uniform(0, 20), 2),
        "descripcion": "clima variable"
    })

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

print("📊 1000 registros generados")