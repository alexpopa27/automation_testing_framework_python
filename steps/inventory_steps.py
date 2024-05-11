from behave import *


@when('inventory: I click on a product')
def step_impl(context):
    context.inventory_page.click_first_item()


@when('inventory: I click on "Back to products"')
def step_impl(context):
    context.inventory_page.click_back_to_products()


@when('inventory: I click on settings icon')
def step_impl(context):
    context.inventory_page.click_settings_icon()


@when('inventory: I click on the shopping cart icon')
def step_impl(context):
    context.inventory_page.click_shopping_cart_icon()


@when('inventory: I add to cart the first item')
def step_impl(context):
    context.inventory_page.add_first_item_in_cart()


@then('inventory: The URL has changed')
def step_impl(context):
    context.inventory_page.item_URL()


@then('inventory: Settings list is displayed')
def step_impl(context):
    context.inventory_page.settings_list_is_displayed()


@then('cart: The URL has changed')
def step_impl(context):
    context.inventory_page.check_shopping_cart_URL()


@then('cart: Items are in the cart')
def step_impl(context):
    context.inventory_page.find_item_in_cart()
