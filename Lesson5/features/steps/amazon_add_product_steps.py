from behave import when, then
from Lesson5.features.pages.amazon_add_product_page import AmazonAddProductToCart


@when('Search for "{product}"')
def search_product(context, product):
    context.amazon_page = AmazonAddProductToCart(context)
    context.amazon_page.search_for_product(product)


@when('Choose the first search result')
def choose_first_search_result(context):
    context.amazon_page.choose_first_search_result()


@when('Add the product to the cart')
def add_product_to_cart(context):
    context.amazon_page.add_product_to_cart()


@when('The cart count should be greater than 0')
def verify_cart_count(context):
    cart_count = context.amazon_page.get_cart_count()
    assert cart_count > 0, "Expected cart count to be greater than 0."


@then('"{product}" should be present in the cart')
def verify_product_in_cart(context, product):
    product_in_cart = context.amazon_page.check_product_in_cart(product)
    assert product_in_cart, f"Expected product '{product}' not found in cart."
