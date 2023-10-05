import celery
from tasks import reverse_string, add
import pytest
from tasks import add
from celery.contrib.pytest import celery_app


## Running Celery Task with Backend and Broker (RabbitMQ)
# @pytest.mark.celery(result_backend="rpc://")
# def test_reverse_string(celery_app, celery_worker):
#     assert reverse_string.delay("hello").get(timeout=10) == "olleh"


@pytest.fixture
def mocked_reverse_string(mocker):
    # Mock the Celery task
    return mocker.patch("tasks.reverse_string.delay", return_value="olleh")


def test_reverse_string_mocked(mocked_reverse_string):
    # Call the Celery task
    result = reverse_string.delay("hello")

    # Check if the Celery task was called once with the correct arguments
    mocked_reverse_string.assert_called_once_with("hello")

    # Check the result of the Celery task
    assert result == "olleh"


def test_add_async_mocked(mocker):
    # Arrange
    x = 5
    y = 7

    # Mock the Celery task's apply_async method
    mocked_add = mocker.patch("tasks.add.apply_async", autospec=True)

    # Act
    result = add.apply_async(args=[x, y])

    # Assert
    mocked_add.assert_called_once_with(args=[x, y])
