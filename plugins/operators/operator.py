from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults

from hooks.hook import MyHook


class MyOperator(BaseOperator):

    @apply_defaults
    def __init__(self, my_field, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_field = my_field

    def execute(self, context):
        hook = MyHook('my_conn')
        hook.my_method()
