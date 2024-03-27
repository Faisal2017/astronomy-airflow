# Sensor checks  if _condition is true every 60 seconds by default (poke_interval)
# Since _condition always returns False, the Sensor will continue checking every 60 sec until it times out after 7 days

from datetime import datetime

from airflow import DAG
from airflow.sensors.python import PythonSensor


def _condition():
    return False


with DAG(
        dag_id="sensor",
        start_date=datetime(2021, 1, 1),
        schedule="@daily",
        catchup=False,
):
    waiting_for_condition = PythonSensor(
        task_id="waiting_for_condition",
        python_callable=_condition,
        poke_interval=60,
        timeout=7 * 24 * 60 * 60
    )
