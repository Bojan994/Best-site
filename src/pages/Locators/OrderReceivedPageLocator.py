from selenium.webdriver.common.by import By


class OrderReceivedPageLocator:
    PAGE_MAIN_HEADER = (By.CSS_SELECTOR, "#post-8 > header > h1")
    ORDER_NUMBER = (By.CSS_SELECTOR,"#post-8 > div > div > div > ul > li.woocommerce-order-overview__order.order > strong")

