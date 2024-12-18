from behave import *
from unittest.mock import patch
import requests

def check_user(username):
    response = requests.get(f"https://api.example/com/users/{username}")
    if response.status_code == 200:
        return "User exists"
    return "User not found"

@given('aplikacja łączy się z API użytkowników')
def step_mock_api(context):
    context.requests_get_patcher = patch('requests.get')
    context.mock_get = context.requests_get_patcher.start()

@when('sprawdzam użytkownika "{username}"')
def step_check_user(context,username):
    context.mock_get.return_value.status_code = 200
    context.response = check_user(username)

@then('odpowiedź powinna zawierać "{expected_response}"')
def step_check_response(context,expected_response):
    assert context.response == expected_response,f"Otrzymano {context.response}"
    context.requests_get_patcher.stop()