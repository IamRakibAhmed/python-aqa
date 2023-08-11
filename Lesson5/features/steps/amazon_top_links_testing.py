from selenium.webdriver.common.by import By
from behave import given, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

AMAZON_BEST_SELLER_LINK = 'https://www.amazon.com/gp/bestsellers/'
TOP_LINKS = (By.CSS_SELECTOR, "#zg_header a")
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')


@given('Open Amazon Bestsellers')
def open_amazon_bestsellers(context):
    context.driver.get(AMAZON_BEST_SELLER_LINK)


@then('User can click through top links and verify the opened page')
def click_through_top_links(context):
    top_links = context.driver.find_elements(*TOP_LINKS)
    wait = WebDriverWait(context.driver, 10)

    for i in range(len(top_links)):
        link_to_click = context.driver.find_elements(*TOP_LINKS)[i]
        link_text = link_to_click.text
        link_to_click.click()

        wait.until(EC.text_to_be_present_in_element(HEADER, link_text))
        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected {link_text} to be in {header_text}'
