from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

from Lesson.features.pages.amazon_orders_page import AmazonOrdersPage
from Lesson.features.pages.amazon_shopping_cart import AmazonPage


@given('Open Amazon page')
def open_amazon(context):
    context.amazon_page = AmazonPage(context.driver)
    context.amazon_page.open_amazon_page()


@when('Click Amazon Orders link')
def click_amazon_orders(context):
    context.orders_page = AmazonOrdersPage(context.driver)
    context.orders_page.click_amazon_orders_link()


@then('Verify Sign In page is opened')
def verify_sign_in_page(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.url_contains('signin'))
