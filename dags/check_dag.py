from datetime import datetime
from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

with DAG(
        dag_id='check_dag',
        start_date=datetime(2024, 1, 1),
        description='DAG to check data',
        schedule_interval='@daily',
        catchup=False,
        tags=['data_engineering'],
        default_args={
            "owner": "data_engineering",
            "retries": 2,
        }
) as DAG:
    create_file = BashOperator(
        task_id="create_file",
        bash_command="echo 'Hi there!' > /tmp/dummy",
    )

    check_file = BashOperator(
        task_id="check_file",
        bash_command="test -f /tmp/dummy"
    )

    read_and_print = PythonOperator(
        task_id='read_and_print',
        python_callable=lambda: print(open('/tmp/dummy', 'rb').read())
    )

    create_file >> check_file >> read_and_print
