import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Lesson4.configuration.Config import Config


class AmazonCartVerificationTest:
    def __init__(self):
        service = Service(Config.CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)

    def open_homepage(self):
        self.driver.get(Config.AMAZON_HOMEPAGE)

    def search_for_product(self, product):
        search_box = self.driver.find_element(*Config.SEARCH_BOX_ID)
        search_box.clear()
        search_box.send_keys(product)
        search_box.submit()

    def choose_first_search_result(self):
        first_result = self.driver.find_element(*Config.FIRST_RESULT_CSS_SELECTOR)
        first_result.click()

    def add_product_to_cart(self):
        add_to_cart_button = self.driver.find_element(*Config.ADD_TO_CART_ID)
        add_to_cart_button.click()
        time.sleep(3)

    def get_cart_count(self):
        cart_count_element = self.driver.find_element(*Config.CART_COUNT)
        cart_count = int(cart_count_element.text)
        return cart_count

    def check_product_in_cart(self, product):
        self.driver.get(Config.AMAZON_CART_LINK)
        cart_items = self.driver.find_elements(*Config.CART_ITEM_CSS_SELECTOR)
        cart_item_names = [item.text for item in cart_items]
        self.driver.quit()
        return product in cart_item_names
