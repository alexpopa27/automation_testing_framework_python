from behave import *

@when('cart: I click on "Continue Shopping"')
def step_impl(context):
    context.cart_page.click_continue_shopping()

@when('cart: I click on "Checkout"')
def step_impl(context):
    context.cart_page.click_on_checkout()

@then('checkout: The URL has changed')
def step_impl(context):
    context.cart_page.checkout_URL_change()