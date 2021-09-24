from airflow.hooks.base import BaseHook


class MyHook(BaseHook):

    def my_method(self):
        print("hello hook")
