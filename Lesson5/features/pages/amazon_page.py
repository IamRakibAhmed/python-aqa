from selenium.webdriver.common.by import By


class AmazonPage:
    AMAZON_LINK = 'https://www.amazon.com/'
    CART_ICON = (By.ID, 'nav-cart-count')
    EMPTY_CART_TEXT = (By.XPATH, "//*[@id='sc-active-cart']/div/div/div[2]/div[1]/h2")

    def __init__(self, context):
        self.driver = context.driver

    def open_amazon_page(self):
        self.driver.get(self.AMAZON_LINK)

    def click_cart_icon(self):
        self.driver.find_element(*self.CART_ICON).click()

    def is_empty_cart_text_present(self):
        return self.driver.find_element(*self.EMPTY_CART_TEXT).is_displayed()
