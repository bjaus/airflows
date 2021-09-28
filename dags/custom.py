from datetime import datetime, timedelta

from airflow import DAG

from operators.hello import HelloOperator
from operators.operator import MyOperator
from sensors.sensor import MySensor

# Can you see me?

DEFAULT_ARGS = {
    "owner": "bos",
    "depends_on_past": False,
    "start_date": datetime(2021, 9, 24),
    "email_on_failure": True,
    "email_on_retry": True,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "customdag",
    max_active_runs=3,
    schedule_interval="@once",
    default_args=DEFAULT_ARGS,
) as dag:

    sens = MySensor(
        task_id="taskA",
    )

    op = MyOperator(
        task_id="taskB",
        my_field="some text",
    )

    hello = HelloOperator(
        task_id="hello-task",
        name="foo_bar",
    )

    sens >> op >> hello
