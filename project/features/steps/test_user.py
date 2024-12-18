from pytest_bdd import given, when, then, scenarios, parsers

from app import get_user_data

scenarios("../user.feature")

@given(parsers.parse("istnieje użytkownik o ID {user_id:d}"))
def step_given_user_exists(mocker,context, user_id):
    context.mocker = mocker
    context.user_id = user_id
    context.mock_get = context.mocker.patch("app.requests.get")
    context.mock_get.return_value.status_code = 200
    context.mock_get.return_value.json.return_value = {
        "id": user_id,
        "name": "John Doe"
    }

@given(parsers.parse("nie istnieje użytkownik o ID {user_id:d}"))
def step_given_user_does_not_exist(mocker,context, user_id):
    context.mocker = mocker
    context.user_id = user_id
    context.mock_get = context.mocker.patch("app.requests.get")
    context.mock_get.return_value.status_code = 404


@when("pobiorę dane użytkownika")
def step_when_fetch_user_data(context):
    context.result = get_user_data(context.user_id)

@then(parsers.parse('dane użytkownika powinny zawierać nazwę "{expected_name}"'))
def step_then_user_data_should_have_name(context, expected_name):
    assert context.result["name"] == expected_name, f"Oczekiwano {expected_name}, otrzymano {context.result}"

@then("dane użytkownika powinny być puste")
def step_then_user_data_should_be_empty(context):
    assert context.result is None, f"Oczekiwano pustego wyniku, otrzymano {context.result}"

