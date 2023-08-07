from selenium.webdriver.common.by import By


class Config:
    CHROME_DRIVER_PATH = './chromedriver.exe'
    AMAZON_HOMEPAGE = "https://www.amazon.com/"
    AMAZON_BEST_SELLERS_LINK = "https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers"
    AMAZON_CART_LINK = "https://www.amazon.com/gp/cart/view.html"
    AMAZON_CUSTOMER_SERVICE_LINK = "https://www.amazon.com/gp/help/customer/display.html"
    BEST_SELLERS_TAB_CLASSNAME = (By.CLASS_NAME, "_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq")
    LINK_TAG_NAME = (By.TAG_NAME, "a")
    SEARCH_BOX_ID = (By.ID, "twotabsearchtextbox")
    FIRST_RESULT_CSS_SELECTOR = (By.CSS_SELECTOR, "div[data-asin] a.a-link-normal")
    ADD_TO_CART_ID = (By.ID, "add-to-cart-button")
    CART_ITEM_CSS_SELECTOR = (By.CSS_SELECTOR, ".a-truncate-cut")
    CART_COUNT = (By.ID, "nav-cart-count")
    CUSTOMER_SERVICE_ISSUE_CARD_CLASS = (By.CLASS_NAME, "issue-card-container")
    CUSTOMER_SERVICE_HELP_SEARCH_BAR_ID = (By.ID, "hubHelpSearchInput")
    CUSTOMER_SERVICE_HELP_TOPICS_CLASS = (By.CLASS_NAME, "help-topics")
