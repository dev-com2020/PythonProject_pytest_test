from behave import given, when, then
from unittest.mock import MagicMock
from user_service import UserService

@given('Konfiguracja środowiska pocztowego')
def step_impl(context):
    context.mail_service = MagicMock()
    context.user_service = UserService(context.mail_service)

@given('System pocztowy jest skonfigurowany')
def step_impl(context):
    context.mail_service.register_user(send_mail=MagicMock())


@when('Użytkownik rejestruje się z e-mailem "{email}"')
def step_impl(context, email):
    context.user_service.register_user(email)


@then('Powinna zostać wysłana jedna wiadomość potwierdzająca')
def step_impl(context):
    context.mail_service.send_email.assert_called_once_with(
        "test@example.com", "Witamy w naszej aplikacji!"
    )
