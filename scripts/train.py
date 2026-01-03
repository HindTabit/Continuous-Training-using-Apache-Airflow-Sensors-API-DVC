import pandas as pd
import requests
import joblib
from sklearn.linear_model import LinearRegression
from pathlib import Path

# Création des dossiers si inexistants
Path("data").mkdir(exist_ok=True)
Path("models").mkdir(exist_ok=True)

# ======================
# 1️⃣ Récupération des données depuis l'API
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

# Sauvegarde des données
df.to_csv("data/weather.csv", index=False)
print("✅ Données sauvegardées : data/weather.csv")

# ======================
# 2️⃣ Entraînement du modèle
# ======================
X = [[i] for i in range(len(df))]
y = df["temperature"]

model = LinearRegression()
model.fit(X, y)

# Sauvegarde du modèle
joblib.dump(model, "models/model.pkl")
print("✅ Modèle entraîné et sauvegardé : models/model.pkl")
