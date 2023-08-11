from selenium.webdriver.common.by import By


class AmazonOrdersPage:
    AMAZON_ORDERS_LINK = (By.XPATH, "//a[contains(@href, '/gp/css/order-history')]")

    def __init__(self, context):
        self.driver = context.driver

    def click_amazon_orders_link(self):
        self.driver.find_element(*self.AMAZON_ORDERS_LINK).click()