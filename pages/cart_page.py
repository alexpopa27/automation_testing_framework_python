from selenium.webdriver.common.by import By
from browser import Browser
from time import sleep

class CartPage(Browser):

    CONTINUE_SHOPPING_BTN = (By.XPATH, '//button[@id="continue-shopping"]')
    CHECKOUT_BTN = (By.XPATH, '//button[@id="checkout"]')

    def click_continue_shopping(self):
        self.driver.find_element(*self.CONTINUE_SHOPPING_BTN).click()

    def click_on_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BTN).click()
        sleep(1.5)

    def checkout_URL_change(self):
        expected = 'https://www.saucedemo.com/checkout-step-one.html'
        actual = self.driver.current_url

        assert actual == expected, 'The URL is wrong'