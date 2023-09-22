from time import sleep
from celery import Celery, shared_task


app = Celery("tasks", backend="rpc://", broker="pyamqp://guest@localhost//")


@app.task
def reverse_string(my_string: str):
    return my_string[::-1]
