from behave import given, then
from Lesson4.test.AmazonCustomerServiceTest import CustomerServicePage


class AmazonCustomerServiceSteps:
    @given('I am on the Customer Service page')
    def open_customer_service_page(context):
        context.amazon_page = CustomerServicePage()
        context.amazon_page.open_customer_service_page()

    @then('I verify the "{title}" title is present')
    def verify_title_present(context, title):
        assert context.amazon_page.verify_title_present(title), f"Title '{title}' is not present."

    @then('I verify the Issue Card UI elements are present')
    def verify_issue_card_elements(context):
        context.amazon_page.verify_issue_card_elements_present()

    @then('I verify the Help Search bar is present')
    def verify_help_search_bar_present(context):
        context.amazon_page.verify_help_search_bar_present()

    @then('I verify the Help Topics UI elements are present')
    def verify_help_topics_elements(context):
        context.amazon_page.verify_help_topics_elements_present()
