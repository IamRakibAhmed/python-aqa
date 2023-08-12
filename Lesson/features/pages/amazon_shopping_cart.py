from selenium.webdriver.common.by import By
from Lesson.features.pages.base_page import BasePage


class AmazonPage(BasePage):
    AMAZON_LINK = 'https://www.amazon.com/'
    CART_ICON = (By.ID, 'nav-cart-count')
    EMPTY_CART_TEXT = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")

    def open_amazon_page(self):
        self.open_url(self.AMAZON_LINK)

    def click_cart_icon(self):
        self.click(self.CART_ICON)

    def is_empty_cart_text_present(self):
        return self.is_displayed(self.EMPTY_CART_TEXT)
