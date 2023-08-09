from behave import *
from selenium.webdriver.common.by import By

PRODUCT_LINK = 'https://www.amazon.com/gp/product/B07BJKRR25/'
COLOR_FINDER_CLASS = (By.CLASS_NAME, 'swatchAvailable')
COLOR_HIGHLIGHTER_CLASS = (By.CLASS_NAME, 'a-button-selected')


@given('I am on the product page')
def go_to_product_page(context):
    context.driver.get(PRODUCT_LINK)


@when('I select each available color')
def select_product_color(context):
    color_swatches = context.driver.find_elements(*COLOR_FINDER_CLASS)
    for swatch in color_swatches:
        swatch.click()


@then('the selected color should be highlighted')
def verify_selected_color(context):
    selected_color = context.driver.find_element(*COLOR_HIGHLIGHTER_CLASS)
    assert selected_color.is_displayed()
