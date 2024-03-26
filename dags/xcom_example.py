# Xcom is a way to communicate between tasks
# as they are independent and could be running on separate machines


from airflow import DAG
from airflow.decorators import task

from datetime import datetime

with DAG(
        dag_id='xcom_example',
        start_date=datetime(2024, 1, 1),
        schedule_interval='@daily',
        catchup=False,
):
    @task
    def peter_task(ti=None):
        return 'iphone'


    @task
    def bryan_task(moble_phone):
        print(moble_phone)


    bryan_task(peter_task())

# above will return 'iphone' when run and this can be seen in Admin -> XComs. return_value is default key

