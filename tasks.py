from time import sleep
from celery import Celery, shared_task
from asyncio import sleep


app = Celery("tasks", backend="rpc://", broker="pyamqp://guest@localhost//")


@app.task
def reverse_string(my_string: str):
    return my_string[::-1]


@app.task
async def return_hello():
    await sleep(1)
    return "hello"
