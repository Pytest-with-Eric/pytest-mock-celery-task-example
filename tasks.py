import time
from celery import Celery, shared_task


app = Celery("tasks", backend="rpc://", broker="pyamqp://guest@localhost//")


@app.task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@app.task
def return_hello():
    return "hello"
