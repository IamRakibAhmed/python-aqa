from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

SIGN_IN_LINK = 'https://www.amazon.com/ap/signin?'
SIGN_IN_BUTTON = (By.CSS_SELECTOR, '#nav-signin-tooltip span.nav-action-inner')


@when('Click Sign In from popup')
def click_sign_in(context):
    wait = WebDriverWait(context.driver, 10)
    sign_in_popup_button = wait.until(EC.element_to_be_clickable(SIGN_IN_BUTTON))
    sign_in_popup_button.click()


@then('Verify Sign In page opens')
def sign_in_page_open(context):
    context.driver.wait.until(EC.url_contains(SIGN_IN_LINK))
