from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

AMAZON_TC_URL = "https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088"
AMAZON_PRIVACY_NOTICE_XPATH = (By.XPATH, "//a[contains(@href, '/privacy')]")


original_window = None
new_window = None


@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get(AMAZON_TC_URL)


@when('Store original window')
def store_original_window(context):
    global original_window
    original_window = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def go_to_amazon_privacy_notice(context):
    amazon_privacy_notice = context.driver.find_element(*AMAZON_PRIVACY_NOTICE_XPATH)
    amazon_privacy_notice.click()
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.number_of_windows_to_be(2))


@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    global new_window
    new_window = [window for window in context.driver.window_handles if window != original_window][0]
    context.driver.switch_to.window(new_window)


@then('Verify Amazon Privacy Notice page is opened')
def verify_notice_page_opened(context):
    new_window_title = context.driver.title
    assert "Privacy Notice" in new_window_title


@then('User can close new window and switch back to original')
def close_new_switch_original(context):
    context.driver.close()
    context.driver.switch_to.window(original_window)
