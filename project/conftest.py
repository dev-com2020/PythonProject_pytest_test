import pytest
from pytest_mock import mocker


@pytest.fixture(scope="function", autouse=True)
def context():
    class Context(object):
        from behave.runner import Context
        Context.mocker = mocker
    return Context()
