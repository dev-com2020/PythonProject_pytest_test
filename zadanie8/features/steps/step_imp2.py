
from behave import given, when, then
from stubs import StubQueryHandler
from queries import PobierzFlapQuery

@given('istnieje Flap o identyfikatorze {flap_id:d}')
def step_given_flap_exists(context, flap_id):
    context.flap_id = flap_id

@when('użytkownik wysyła zapytanie o ten Flap')
def step_when_user_queries_flap(context):
    context.query_handler = StubQueryHandler()
    zapytanie = PobierzFlapQuery(context.flap_id)
    context.result = context.query_handler.handle(zapytanie)

@then('powinien otrzymać Flap o nazwie "{expected_name}"')
def step_then_should_receive_flap(context, expected_name):
    assert context.result['nazwa'] == expected_name
