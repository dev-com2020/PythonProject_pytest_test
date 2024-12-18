from unittest.mock import patch

def before_tag(context,tag):
    if tag == "system":
        print("System is ready!")
        # context.requests_get_patcher = patch('requests.get')
        # context.mock_get = context.requests_get_patcher.start()
        context.scenario.skip("Scenariusz pominięto z powodu taga")

# def after_all(context):
#     context.requests_get_patcher.stop()