from browser import Browser
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.inventory_page = InventoryPage()
    context.cart_page = CartPage()
    context.checkout_page = CheckoutPage()


def after_all(context):
    context.browser.close()
