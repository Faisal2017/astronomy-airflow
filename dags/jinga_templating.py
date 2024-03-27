# Note - DAG requires a Variable called ml_model_parameters
# can be created though airflow UI: Admin -> Variables -> Add
# or by adding to env file and restarting: AIRFLOW_VAR_ML_MODEL_PARAMETERS='{"param": [100, 150, 200]}'

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable


def _ml_task(ml_parameter):
    print(ml_parameter)


with DAG(
        dag_id='jinga_templating',
        start_date=datetime(2024, 1, 1),
        schedule_interval='@daily',
        catchup=False
) as dag:
    ml_tasks = []

    for ml_parameter in Variable.get('ml_model_parameters', deserialize_json=True)["param"]:
        ml_tasks.append(PythonOperator(
            task_id=f'ml_task_{ml_parameter}',
            python_callable=_ml_task,
            op_kwargs={
                'ml_parameter': ml_parameter
            }
        ))

    ml_tasks
