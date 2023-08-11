from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

from Lesson5.features.pages.amazon_orders_page import AmazonOrdersPage
from Lesson5.features.pages.amazon_page import AmazonPage


@given('Open Amazon page')
def open_amazon(context):
    context.amazon_page = AmazonPage(context)
    context.amazon_page.open_amazon_page()


@when('Click Amazon Orders link')
def click_amazon_orders(context):
    context.orders_page = AmazonOrdersPage(context)
    context.orders_page.click_amazon_orders_link()


@then('Verify Sign In page is opened')
def verify_sign_in_page(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.url_contains('signin'))
