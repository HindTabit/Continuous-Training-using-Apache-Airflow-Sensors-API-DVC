import pandas as pd
import requests
import joblib
from sklearn.linear_model import LinearRegression
from pathlib import Path
import os

# On définit explicitement le dossier racine dans le conteneur
BASE_DIR = Path("/opt/airflow")

# Création des dossiers avec des chemins absolus
data_dir = BASE_DIR / "data"
models_dir = BASE_DIR / "models"

data_dir.mkdir(parents=True, exist_ok=True)
models_dir.mkdir(parents=True, exist_ok=True)

# ======================
# 1️⃣ Récupération des données
# ======================
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 31.63,
    "longitude": -8.00,
    "hourly": "temperature_2m"
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature": data["hourly"]["temperature_2m"]
})

# Sauvegarde avec chemin absolu
data_file = data_dir / "weather.csv"
df.to_csv(data_file, index=False)
print(f"✅ Données sauvegardées : {data_file}")

# ======================
# 2️⃣ Entraînement du modèle
# ======================
X = [[i] for i in range(len(df))]
y = df["temperature"]

model = LinearRegression()
model.fit(X, y)

# Sauvegarde avec chemin absolu
model_file = models_dir / "model.pkl"
joblib.dump(model, model_file)
print(f"✅ Modèle entraîné et sauvegardé : {model_file}")