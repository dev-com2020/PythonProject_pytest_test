from behave import *

@given('User is on Payment screen')
def step_impl(context):
    print('STEP: Given User is on Payment screen')


@when('User clicks on Payment types')
def step_impl(context):
    print('STEP: When User clicks on Payment types')


@then('User should get Types cash method')
def step_impl(context):
    print('STEP: Then User should get Types cash method')
