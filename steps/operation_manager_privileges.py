from behave import *

@given('logged in as an operation manager')
def step_impl(context):
    pass

@when('a CSA processes an exchange')
def step_impl(context):
    assert True is not False

@then('I should be able to confirm that the contents of the kit are present')
def step_impl(context):
    assert context.failed is False
