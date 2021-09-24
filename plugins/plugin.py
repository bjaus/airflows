from airflow.plugins_manager import AirflowPlugin

from hooks.hook import MyHook
from operators.gooddata import GoodDataOperator
from operators.hello_operator import HelloOperator
from operators.operator import MyOperator
from operators.zendesk import ZendeskOperator
from sensors.sensor import MySensor


class PluginName(AirflowPlugin):

    name = "plugin"

    hooks = [
        MyHook,
    ]
    operators = [
        GoodDataOperator,
        HelloOperator,
        MyOperator,
        ZendeskOperator,
    ]
    sensors = [
        MySensor,
    ]
