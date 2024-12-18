from behave import *

@given('user enters "{name}" and "{password}"')
def step_imp(context,name,password):
    print("Username for login: {} ".format(name))
    print(f"Pass for login: {password}")

@then('user should be logged in')
def step_imp(context):
    pass