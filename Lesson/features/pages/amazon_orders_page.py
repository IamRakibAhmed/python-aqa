from selenium.webdriver.common.by import By
from Lesson.features.pages.base_page import BasePage


class AmazonOrdersPage(BasePage):
    AMAZON_ORDERS_LINK = (By.ID, "nav-orders")

    def click_amazon_orders_link(self):
        self.click(self.AMAZON_ORDERS_LINK)
