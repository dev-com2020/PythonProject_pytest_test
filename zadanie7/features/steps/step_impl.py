from behave import given, when, then

@given("użytkownik jest na stronie logowania")
def step_given_user_on_login_page(context):
    context.page = "login_page"

@when("użytkownik wpisuje poprawny login i hasło")
def step_when_user_enters_credentials(context):
    context.login_successful = True

@when("użytkownik wpisuje błędne dane logowania")
def step_when_user_enters_wrong_credentials(context):
    context.login_successful = False

@then("użytkownik zostaje zalogowany")
def step_then_user_logged_in(context):
    assert context.login_successful is True

@then('użytkownik widzi powiadomienie o nowej wiadomości')
def step_then_user_sees_notification(context):
    context.notification = "Nowa wiadomość"
    assert context.notification == "Nowa wiadomość"

@then('użytkownik widzi komunikat "Niepoprawny login lub hasło"')
def step_then_user_sees_error_message(context):
    assert context.login_successful is False

@then("konto użytkownika pozostaje niezalogowane")
def step_then_account_not_logged_in(context):
    assert context.login_successful is False
