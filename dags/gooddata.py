from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

from operators.zendesk import ZendeskOperator
from operators.gooddata import GoodDataOperator


default_args = {
    "owner": "bos",
    "depends_on_past": False,
    "email": [
        "bjaus@getaroom.com",
    ],
    "email_on_failure": True,
    "email_on_retry": True,
    "retries": 5,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "gooddata-and-zendesk",
    default_args=default_args,
    description="Testing getting access to custom plugins",
    schedule_interval=timedelta(hours=1),
    start_date=days_ago(1),
    tags=[
        "bos",
        "gooddata",
        "zendesk",
    ],
) as dag:

    task1 = BashOperator(
        task_id="announcement",
        bash_command="echo 'Running gooddata task...'",
    )

    task2 = GoodDataOperator(
        task_id="gooddata-hello",
        name="GoodData",
    )

    task3 = ZendeskOperator(
        task_id="zendesk-hello",
        name="Zendesk",
    )

    task1 >> task2 >> task3
