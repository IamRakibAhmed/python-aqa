from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

AMAZON_HOMEPAGE = 'https://www.amazon.com'
SEARCH_BAR_ID = (By.ID, 'twotabsearchtextbox')
PRODUCT_NAMES_XPATH = (By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
PRODUCT_IMAGES_XPATH = (By.XPATH, "//img[@class='s-image']")


@given('I am on the Amazon homepage')
def go_to_amazon_homepage(context):
    context.driver.get(AMAZON_HOMEPAGE)


@when('I search for "{keyword}" using the search bar')
def search_product(context, keyword):
    search_bar = context.driver.find_element(*SEARCH_BAR_ID)
    search_bar.send_keys(keyword)
    search_bar.send_keys(Keys.ENTER)
    wait = WebDriverWait(context.driver, 10)
    search_results_loaded = wait.until(EC.title_contains(keyword))
    assert search_results_loaded, f"Search results for '{keyword}' not loaded"


@then('I should see a list of search results')
def verify_search_result(context):
    assert "Amazon.com : laptop" in context.driver.title


@then('each search result should have a product name')
def verify_product_names(context):
    product_names = context.driver.find_elements(*PRODUCT_NAMES_XPATH)
    for name in product_names:
        assert name.text.strip() != ""


@then('each search result should have a product image')
def verify_product_images(context):
    product_images = context.driver.find_elements(*PRODUCT_IMAGES_XPATH)
    for image in product_images:
        assert image.get_attribute("src") != ""


@then('I close the browser')
def close_browser(context):
    context.driver.quit()
