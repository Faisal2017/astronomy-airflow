from airflow import DAG
from airflow.operators.python import PythonOperator

import pendulum


def _transform(ti):
    import requests
    response = requests.get('https://swapi.dev/api/people/1').json()
    print(response)

    my_character = {}
    my_character["height"] = int(response["height"]) - 20
    my_character["mass"] = int(response["mass"]) - 50
    my_character["hair_color"] = "black" if response["hair_color"] == "blond" else "blond"
    my_character["eye_color"] = "hazel" if response["eye_color"] == "blue" else "blue"
    my_character["gender"] = "female" if response["gender"] == "male" else "female"

    ti.xcom_push("character_info", my_character)


def _load(ti):
    print(ti.xcom_pull(key='character_info', task_ids='_transform'))


with DAG(
        'xcom_example_2',
        schedule=None,
        start_date=pendulum.datetime(2024, 3, 1),
        catchup=False
):
    t1 = PythonOperator(
        task_id='_transform',
        python_callable=_transform
    )

    t2 = PythonOperator(
        task_id='load',
        python_callable=_load
    )

    t1 >> t2