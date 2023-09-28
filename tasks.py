from time import sleep
from celery import Celery, shared_task
from asyncio import sleep
from asgiref.sync import async_to_sync
import asyncio


app = Celery("tasks", backend="rpc://", broker="pyamqp://guest@localhost//")


@app.task
def reverse_string(my_string: str):
    return my_string[::-1]


@app.task(bind=True)
def add(self, x, y):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    async def async_add(x, y):
        return x + y

    result = loop.run_until_complete(async_add(x, y))
    loop.close()
    return result
