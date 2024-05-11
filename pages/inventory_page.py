from selenium.webdriver.common.by import By
from browser import Browser
from time import sleep


class InventoryPage(Browser):
    BACK_TO_PRD_BUTTON = (By.XPATH, '//button[@id="back-to-products"]')
    SETTINGS_ICON = (By.XPATH, '//button[@id="react-burger-menu-btn"]')
    SETTINGS_LIST = (By.XPATH, '//nav[@class="bm-item-list"]')
    SHOPPING_CART_ICON = (By.XPATH, '//a[@class="shopping_cart_link"]')

    def click_first_item(self):
        self.driver.find_element(By.LINK_TEXT, 'Sauce Labs Backpack').click()
        sleep(1)

    def item_URL(self):
        expected = 'https://www.saucedemo.com/inventory-item.html?id=4'
        actual = self.driver.current_url

        assert expected == actual, f'The URL is wrong, expected: {expected}, actual: {actual}'

    def click_back_to_products(self):
        self.driver.find_element(*self.BACK_TO_PRD_BUTTON).click()

    def click_settings_icon(self):
        self.driver.find_element(*self.SETTINGS_ICON).click()
        sleep(1.5)

    def settings_list_is_displayed(self):
        actual = self.driver.find_element(*self.SETTINGS_LIST).is_displayed()
        expected = True

        assert expected == actual, f'Settings list is not displayed, expected: {expected}, actual: {actual}'

    def click_shopping_cart_icon(self):
        self.driver.find_element(*self.SHOPPING_CART_ICON).click()

    def check_shopping_cart_URL(self):
        expected = 'https://www.saucedemo.com/cart.html'
        actual = self.driver.current_url

        assert expected == actual, f'The URL is wrong, expected: {expected}, actual: {actual}'

    def add_first_item_in_cart(self):
        self.driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]').click()
        sleep(1.5)

    def find_item_in_cart(self):
        actual = self.driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text
        expected = 'Sauce Labs Backpack'

        assert actual == expected, 'Item is not in cart'
