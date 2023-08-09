from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Lesson4.configuration.Config import Config


class CustomerServicePage:
    def __init__(self):
        service = Service(Config.CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)

    def open_customer_service_page(self):
        self.driver.get(Config.AMAZON_CUSTOMER_SERVICE_LINK)

    def verify_title_present(self, title):
        title_element = self.driver.find_element(By.XPATH, f"//*[contains(text(), '{title}')]")
        return title_element.is_displayed()

    def verify_issue_card_elements_present(self):
        issue_card_container = self.driver.find_element(*Config.CUSTOMER_SERVICE_ISSUE_CARD_CLASS)
        return issue_card_container.is_displayed()

    def verify_help_search_bar_present(self):
        search_bar = self.driver.find_element(*Config.CUSTOMER_SERVICE_HELP_SEARCH_BAR_ID)
        return search_bar.is_displayed()

    def verify_help_topics_elements_present(self):
        help_topics_container = self.driver.find_element(*Config.CUSTOMER_SERVICE_HELP_TOPICS_CLASS)
        return help_topics_container.is_displayed()

    def close_browser(self):
        self.driver.quit()
