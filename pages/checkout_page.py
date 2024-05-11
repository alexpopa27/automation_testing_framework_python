from selenium.webdriver.common.by import By
from browser import Browser
from time import sleep

class CheckoutPage(Browser):

    CANCEL_BTN = (By.XPATH, '//button[@id="cancel"]')
    CONTINUE_BTN = (By.XPATH, '//input[@id="continue"]')
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    POSTAL_CODE = (By.NAME, 'postalCode')

    def click_on_cancel(self):
        self.driver.find_element(*self.CANCEL_BTN).click()
        sleep(1.5)

    def click_on_continue(self):
        self.driver.find_element(*self.CONTINUE_BTN).click()
        sleep(1.5)

    def check_error_msg(self, error_msg):
        if error_msg == "Error: First Name is required":
            actual = self.driver.find_element(By.XPATH, '//h3[normalize-space()="Error: First Name is required"]').text

            assert actual == error_msg, 'Error message is incorrect'
        elif error_msg == "Error: Postal Code is required":
            actual = self.driver.find_element(By.XPATH, '//h3[normalize-space()="Error: Postal Code is required"]').text

            assert actual == error_msg, f'Error message is incorrect, expected: {error_msg}, actual: {actual}'


    def complete_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)

    def complete_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)

    def complete_postal_code(self, postal_code):
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def checkout_URL(self):
        expected = 'https://www.saucedemo.com/checkout-step-two.html'
        actual = self.driver.current_url

        assert expected == actual, f'URL is incorrect, actual: {actual}, expected: {expected}'