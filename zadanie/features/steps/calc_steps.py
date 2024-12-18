from behave import *

def add(a,b):
        return a + b


@given('liczby {a:d} i {b:d}')
def step_given_two_numbers(context,a,b):
    context.a = a
    context.b = b

@when('obliczam sumę')
def step_when_calculate_sum(context):
    context.result = add(context.a,context.b)

@then('wynik powinien wynosić {expected_result:d}')
def step_then_check_result(context,expected_result):
    assert context.result == expected_result, f"Oczekiwano {expected_result}, ale otrzymaliśmy {context.result}"