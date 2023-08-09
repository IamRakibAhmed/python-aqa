from behave import given, when, then
from Lesson4.tests.AmazonCartVerificationTest import AmazonCartVerificationTest


@given('I am on the Amazon homepage')
def open_amazon_homepage(context):
    context.amazon_page = AmazonCartVerificationTest()
    context.amazon_page.open_homepage()


@when('I search for "{product}"')
def search_product(context, product):
    context.amazon_page.search_for_product(product)


@when('I choose the first search result')
def choose_first_search_result(context):
    context.amazon_page.choose_first_search_result()


@when('I add the product to the cart')
def add_product_to_cart(context):
    context.amazon_page.add_product_to_cart()


@when('the cart count should be greater than 0')
def verify_cart_count(context):
    cart_count = context.amazon_page.get_cart_count()
    assert cart_count > 0, "Expected cart count to be greater than 0."


@then('I should see the product "{product}" in the cart')
def verify_product_in_cart(context, product):
    product_in_cart = context.amazon_page.check_product_in_cart(product)
    assert product_in_cart, f"Expected product '{product}' not found in cart."
