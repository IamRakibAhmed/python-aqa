from behave import when, then


@when('Click on cart icon')
def click_cart_icon(context):
    context.amazon_page.click_cart_icon()


@then("Verify 'Your Shopping Cart is empty.' text present")
def verify_empty_cart_text(context):
    assert context.amazon_page.is_empty_cart_text_present(), ("Expected 'Your Amazon Cart is empty' text to be "
                                                              "present")
