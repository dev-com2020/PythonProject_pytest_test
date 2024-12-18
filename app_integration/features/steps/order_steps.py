from behave import given, when, then
from unittest.mock import patch
from order_management.app import create_order
from order_management.database import Database

@given("system jest gotowy do obsługi zamówień")
def step_setup_system(context):
    context.db = Database()
    context.db.clear_orders()  # Czyścimy bazę danych
    context.payment_mock = patch('order_management.payment_service.process_payment')
    context.mock_payment = context.payment_mock.start()

@when('tworzę zamówienie na produkt "{product}" o ilości {quantity:d}')
def step_create_order(context, product, quantity):
    context.mock_payment.return_value = True
    context.order = create_order(product, quantity, context.db)


@when("płatność zostaje przetworzona")
def step_process_payment(context):
    assert context.order['payment_status'] == 'Processed'

@then("zamówienie powinno zostać zapisane w bazie danych")
def step_check_order_saved(context):
    saved_order = context.db.get_order(context.order['order_id'])
    assert saved_order is not None, "Zamówienie nie zostało zapisane"
    assert saved_order['product'] == context.order['product']
    assert saved_order['quantity'] == context.order['quantity']
    context.payment_mock.stop()

