from airflow import DAG
from airflow.operators.python import PythonOperator
from include.helpers import print_msg

from datetime import datetime

with DAG(
        dag_id='my_dag',
        start_date=datetime(2022, 1, 1),
        schedule_interval='@daily',
        catchup=False,
        tags=['my_tag'],
        default_args={
            "owner": "community",  # Defines the value of the "owner" column in the DAG view of the Airflow UI
            "retries": 2,  # If a task fails, it will retry 2 times.
        }
) as DAG:
    task = PythonOperator(
        task_id='task',
        python_callable=print_msg
    )
