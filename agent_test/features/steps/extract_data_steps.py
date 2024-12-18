from behave import given, when, then
from agent.http_agent import HttpAgent

@given("Uruchomiono agenta HTTP")
def step_initialize_agent(context):
    context.agent = HttpAgent()

@when("Otrzymuje odpowiedź HTTP z danymi użytkownika")
def step_receive_http_response(context):
    context.http_response = "HTTP/1.1 200 OK\nImię: Jan\nNazwisko: Kowalski"
    context.extraction_result = context.agent.extract_user_data(context.http_response)

@then('Agent powinien wyodrębnić imię "Jan" i nazwisko "Kowalski"')
def step_validate_extraction(context):
    assert context.extraction_result is True, "Ekstrakcja nie powiodła się"
    assert context.agent.data['first_name'] == "Jan", "Niepoprawne imię"
    assert context.agent.data['last_name'] == "Kowalski", "Niepoprawne nazwisko"