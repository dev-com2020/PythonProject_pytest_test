from behave import *

@given('user enters name and password')
def step_impl(context):
    print("Multiline:" + context.text)

@then('user should be logged')
def step_impl(context):
    pass