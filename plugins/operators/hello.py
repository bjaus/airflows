from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults


class HelloOperator(BaseOperator):

    @apply_defaults
    def __init__(self, name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def execute(self, context):
        message = f"Hello {self.name}!!!"
        print(message)
        return message
