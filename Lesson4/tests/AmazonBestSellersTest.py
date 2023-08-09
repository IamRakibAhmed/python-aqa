import time
from Lesson4.configuration.Config import Config


class AmazonBestSellersTest:
    def __init__(self, driver):
        self.driver = driver

    def open_amazon_best_sellers_page(self):
        self.driver.get(Config.AMAZON_BEST_SELLERS_LINK)

    def verify_links(self, expected_num_links):
        time.sleep(3)
        expected_num_links = int(expected_num_links)
        link_container = self.driver.find_element(*Config.BEST_SELLERS_TAB_CLASSNAME)
        link_elements = link_container.find_elements(*Config.LINK_NAME)
        num_links = len(link_elements)
        assert num_links == expected_num_links, f"Expected {expected_num_links} links, but found {num_links} links."

    def close_browser(self):
        self.driver.quit()
