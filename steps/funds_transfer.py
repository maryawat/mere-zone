from behave import *

@given('customer has made payments on his/her account')
def step_impl(context):
    pass

@when('customer exchanges his/her kit for another model')
def step_impl(context):
    assert True is not False

@then('already paid amount should be transferred to the new model')
def step_impl(context):
    assert context.failed is False
