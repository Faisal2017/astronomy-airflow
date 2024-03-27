# Example of check an S3 bucket for files
# Note - default timeout for Sensors is 7 days

from datetime import datetime

from airflow.decorators import dag, task
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor


@dag(
    dag_id='sensor_example_aws_s3',
    schedule=None,
    start_date=datetime(2023, 1, 1),
    tags=['aws'],
    catchup=False
)
def sensor_example_aws_s3():
    wait_for_file = S3KeySensor(
        task_id="wait_for_file",
        aws_conn_id="aws_s3", # need to create connection with access to S3
        bucket_key="s3://fal-airflow/data_*", # check for files beginning with data_
        wildcard_match=True,
    )

    @task
    def process_file():
        print("I processed the file!")

    wait_for_file >> process_file()


sensor_example_aws_s3()
