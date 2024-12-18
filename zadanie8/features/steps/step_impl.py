from behave import given, when, then

from zadanie8.features.steps.commands import UtworzFlapCommand
from zadanie8.features.steps.mocks import MockCommandHandler


@given('użytkownik chce utworzyć nowy Flap o nazwie "{nazwa_flapa}"')
def step_given_user_wants_to_create_flap(context, nazwa_flapa):
    context.flap_name = nazwa_flapa

@when('wysyła polecenie utworzenia Flapa')
def step_when_user_sends_create_command(context):
    context.command_handler = MockCommandHandler()
    polecenie = UtworzFlapCommand(context.flap_name)
    context.result = context.command_handler.handle(polecenie)

@then('Flap powinien zostać utworzony pomyślnie')
def step_then_flap_should_be_created(context):
    assert context.result == "Flap został utworzony"
    assert context.command_handler.last_command == context.flap_name
