import time

from selenium.webdriver.common.by import By


class AmazonAddProductToCart:
    AMAZON_CART_LINK = "https://www.amazon.com/gp/cart/view.html"

    SEARCH_BOX_ID = (By.ID, "twotabsearchtextbox")
    FIRST_RESULT_CSS_SELECTOR = (By.CSS_SELECTOR, "div[data-asin] a.a-link-normal")
    ADD_TO_CART_ID = (By.ID, "add-to-cart-button")
    CART_COUNT = (By.ID, "nav-cart-count")
    CART_ITEM_CSS_SELECTOR = (By.CSS_SELECTOR, ".a-truncate-cut")

    def __init__(self, context):
        self.driver = context.driver

    def search_for_product(self, product):
        search_box = self.driver.find_element(*self.SEARCH_BOX_ID)
        search_box.clear()
        search_box.send_keys(product)
        search_box.submit()

    def choose_first_search_result(self):
        first_result = self.driver.find_element(*self.FIRST_RESULT_CSS_SELECTOR)
        first_result.click()

    def add_product_to_cart(self):
        add_to_cart_button = self.driver.find_element(*self.ADD_TO_CART_ID)
        add_to_cart_button.click()
        time.sleep(3)

    def get_cart_count(self):
        cart_count_element = self.driver.find_element(*self.CART_COUNT)
        cart_count = int(cart_count_element.text)
        return cart_count

    def check_product_in_cart(self, product):
        self.driver.get(self.AMAZON_CART_LINK)
        cart_items = self.driver.find_elements(*self.CART_ITEM_CSS_SELECTOR)
        cart_item_names = [item.text for item in cart_items]
        return product in cart_item_names
