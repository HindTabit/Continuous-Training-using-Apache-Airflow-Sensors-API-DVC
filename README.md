# Continuous-Training-using-Apache-Airflow-Sensors-API-DVC

## 📌 Description du projet

Ce projet a pour objectif de mettre en place un **pipeline de continuous training pour le Machine Learning** en utilisant les principes du **MLOps**.  
Il repose sur la détection automatique de nouvelles données via une **API météo**, surveillée par des **Airflow Sensors**, déclenchant automatiquement l’entraînement, l’évaluation et le versionnement du modèle.

L’ensemble du workflow est orchestré par **Apache Airflow**, tandis que **DVC** est utilisé pour assurer le suivi des données et des modèles.  
La solution est entièrement **conteneurisée avec Docker**, garantissant la reproductibilité de l’environnement.

---

## 🧠 Architecture du projet

Le flux général du pipeline est le suivant :

- Une API météo fournit de nouvelles données
- Apache Airflow détecte ces données via un **HTTP Sensor**
- Les données sont sauvegardées et versionnées avec **DVC**
- Le modèle de Machine Learning est entraîné automatiquement
- Le modèle entraîné est stocké et versionné

---

## 🌐 API utilisée

Le projet utilise l’API **Open-Meteo** pour récupérer des données météo horaires (température) :
https://api.open-meteo.com/v1/forecastlatitude=31.63&longitude=-8.00&hourly=temperature_2m


Ces données servent d’exemple de flux de données dynamiques déclenchant le pipeline de continuous training.

---

## 🛠️ Technologies utilisées

- Docker & Docker Compose  
- Apache Airflow  
- Python 3.8+  
- Scikit-learn  
- Git  
- DVC  

---

⚠️ **Remarque :** les dossiers `data` et `models` doivent être vides au début avant de lancer le pipeline automatiquement.

---

## 🚀 Lancement du projet

### 1️⃣ Démarrer les services Docker
docker compose up -d

### Entrer dans le container
docker exec -it airflow bash

### Initialiser la base de données Airflow
airflow db init

### Créer un utilisateur Airflow ( vouspouvez changer hind avec le nom de votre propre utilisateur )
airflow users create --username hind --password hind --firstname admin --lastname admin --role Admin --email hindtabit2003@gmail.com

### Accès à l’interface Airflow
http://localhost:8081








