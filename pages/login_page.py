from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from browser import Browser
from time import sleep

class LoginPage(Browser):
    USERNAME = (By.XPATH, '//input[@id="user-name"]')
    PASSWORD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BTN = (By.XPATH, '//input[@id="login-button"]')

    def goto_login_page(self):
        self.driver.get('https://www.saucedemo.com/')

    def username_input(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def password_input(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()


    def check_URL(self):
        expected = 'https://www.saucedemo.com/inventory.html'
        actual = self.driver.current_url
        assert actual == expected, 'The URL is wrong'

    def error_msg_appears(self, expected_msg):
        try:
            actual_msg = self.driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]').text
        except NoSuchElementException:
            actual_msg = 'None'

        assert expected_msg == actual_msg, f'Error message is incorrect, expected: {expected_msg}, actual: {actual_msg}'
