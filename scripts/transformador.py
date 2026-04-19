import pandas as pd

df = pd.read_csv("data.csv")

# Limpieza simple
df.dropna(inplace=True)

df.to_csv("data_transformada.csv", index=False)

print("🔄 Datos transformados")