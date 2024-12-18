from behave import *

@given('I reach office at "{time}" shift')
def step_imp(context,time):
    print("Shift is: {} ".format(time))