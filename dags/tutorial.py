import os
from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

DEFAULT_ARGS = {
    "owner": "bjaus",
    "depends_on_past": False,
    "email": ["bjaus@getaroom.com"],
    "email_on_failure": True,
    "email_on_retry": True,
    "retries": 5,
    "retry_delay": timedelta(minutes=5),
}


def check_env_var(*args, **kwargs):
    var = os.getenv("TEST_VARIABLE")
    print(var)
    return var


def check_pip_install(*args, **kwargs):
    from environs import Env

    env = Env()
    var = env("TEST_VARIABLE", None)
    print(var)
    return var


with DAG(
    "tutorial",
    default_args=DEFAULT_ARGS,
    description="A simple tutorial DAG",
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
) as dag:

    task1 = PythonOperator(
        task_id="check-environment-variables",
        python_callable=check_env_var,
    )

    task2 = PythonOperator(
        task_id="check-pip-installs",
        python_callable=check_pip_install,
    )

    task1 >> task2
