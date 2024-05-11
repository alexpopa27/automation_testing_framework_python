from behave import *

@given('login: I am an user on the login page')
def step_impl(context):
    context.login_page.goto_login_page()

@when('login: I fill the username with value "{username}"')
def step_impl(context, username):
    context.login_page.username_input(username)

@when('login: I fill the password with value "{password}"')
def step_impl(context, password):
    context.login_page.password_input(password)

@when('login: I press the login button')
def step_impl(context):
    context.login_page.click_login()

@then('login: The URL has changed')
def step_impl(context):
    context.login_page.check_URL()

@then('login: Error message appears: "{expected_msg}"')
def step_impl(context, expected_msg):
    context.login_page.error_msg_appears(expected_msg)