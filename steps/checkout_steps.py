from behave import *

@when('checkout: I click on "Cancel"')
def step_impl(context):
    context.checkout_page.click_on_cancel()

@when('checkout: I click on "Continue"')
def step_impl(context):
    context.checkout_page.click_on_continue()

@when('checkout: I fill the first name with value: "{first_name}"')
def step_impl(context, first_name):
    context.checkout_page.complete_first_name(first_name)

@when('checkout: I fill the last name with value: "{last_name}"')
def step_impl(context, last_name):
    context.checkout_page.complete_last_name(last_name)

@when('checkout: I fill the postal code with value: "{postal_code}"')
def step_impl(context, postal_code):
    context.checkout_page.complete_postal_code(postal_code)

@then('checkout: Error message is displayed: "{error_msg}"')
def step_impl(context, error_msg):
    context.checkout_page.check_error_msg(error_msg)

@then('checkout: The URL has changed again')
def step_impl(context):
    context.checkout_page.checkout_URL()