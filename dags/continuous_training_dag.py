from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.http.sensors.http import HttpSensor
from datetime import datetime
import os

# Récupérer le chemin du dossier actuel du DAG
DAG_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
# Chemin vers /opt/airflow/dags
DAG_FOLDER = os.path.dirname(os.path.abspath(__file__))
# Chemin vers la racine /opt/airflow
PROJECT_ROOT = os.path.dirname(DAG_FOLDER)

with DAG(
    dag_id="continuous_training_api_dvc",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@hourly",   # entraînement toutes les heures
    catchup=False
) as dag:

    # 1️⃣ Vérifier que l'API est disponible
    wait_for_api = HttpSensor(
        task_id="wait_for_weather_api",
        http_conn_id="weather_api",
        endpoint="v1/forecast?latitude=31.63&longitude=-8.00&hourly=temperature_2m",
        poke_interval=60,
        timeout=300
    )

    # 2️⃣ Lancer l'entraînement
    train_model = BashOperator(
        task_id="train_model",
        bash_command=f"python {PROJECT_ROOT}/scripts/train.py"
    )

    wait_for_api >> train_model
