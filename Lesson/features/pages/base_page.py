class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def open_url(self, url):
        self.driver.get(url)

    def clear(self, locator):
        self.find_element(locator).clear()

    def submit(self, locator):
        self.find_element(locator).submit()

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)
