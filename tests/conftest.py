import pytest


@pytest.fixture(scope="session")
def celery_config():
    return {"broker_url": "pyamqp://", "result_backend": "rpc://"}
