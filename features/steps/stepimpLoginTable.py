from behave import *


class Depr:
    def __init__(self,username,ms=None):
        if not ms:
            ms = []
            self.username = username
            self.ms = ms
    def m_addition(self,username):
        assert username not in self.ms
        self.ms.append(username)

class LModel:
    def __init__(self):
        self.loginuser = []
        self.password = {}
    def usr_addition(self,username,password):
        assert username not in self.loginuser
        if password not in self.password:
            self.password[password] = Depr(password)
        self.password[password].m_addition(username)


@given('Collection of credentials')
def step_impl(context):
    model = getattr(context,"model", None)
    if not model:
        context.model = LModel()
    for r in context.table:
        context.model.usr_addition(r["username"], password=r["password"])

@then('user should be ok')
def step_impl(context):
    pass