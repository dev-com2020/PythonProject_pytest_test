import pytest

# Integracja pytest z Behave
@pytest.fixture(scope="function", autouse=True)
def inject_mocker(mocker):
    """Inject mocker into Behave context"""
    from behave.runner import Context
    Context.mocker = mocker
