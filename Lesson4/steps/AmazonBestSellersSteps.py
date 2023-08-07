from behave import given, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Lesson4.configuration.Config import Config
from Lesson4.test.AmazonBestSellersTest import AmazonBestSellersTest


class AmazonBestSellersSteps:
    @given('I am on the Amazon BestSellers page')
    def open_amazon_best_sellers_page(context):
        service = Service(Config.CHROME_DRIVER_PATH)
        context.driver = webdriver.Chrome(service=service)
        context.amazon_test = AmazonBestSellersTest(context.driver)
        context.amazon_test.open_amazon_best_sellers_page()

    @then('I should see {expected_num_links} links')
    def verify_links(context, expected_num_links):
        context.amazon_test.verify_links(expected_num_links)
        context.amazon_test.close_browser()
