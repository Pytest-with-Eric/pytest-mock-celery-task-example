import celery
import pytest
from tasks import add, mul


### This works!!
@pytest.mark.celery(result_backend="rpc://")
def test_create_task(celery_app, celery_worker):
    @celery_app.task
    def mul(x, y):
        return x * y

    celery_worker.reload()
    assert mul.delay(4, 4).get(timeout=10) == 16


# This works too!!
# def test_celery_mul(celery_app, celery_worker):
#     assert mul.delay(4, 4).get(timeout=10) == 16


# # This works too!!
# def test_celery_mul2(celery_worker):
#     assert mul.delay(4, 4).get(timeout=10) == 16


# def test_add_task(celery_app, celery_worker):
#     assert add.delay(4, 4).get(timeout=10) == 8

# import pytest
# from celery import Celery
# from tasks import add


# @pytest.fixture(scope="module")
# def celery_app(request):
#     app = Celery("test_tasks", backend="memory", broker="memory://")
#     app.conf.task_always_eager = True
#     return app


# def test_add_task(celery_app):
#     assert add.delay(4, 4).get(timeout=10) == 8
