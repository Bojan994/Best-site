from selenium.webdriver.common.by import By


class CheckoutPageLocator:
    FIRST_NAME = (By.CSS_SELECTOR, "#billing_first_name")
    LAST_NAME = (By.CSS_SELECTOR,"#billing_last_name")
    STREET_ADDRESS= (By.CSS_SELECTOR,"#billing_address_1")
    CITY = (By.CSS_SELECTOR,"#billing_city")
    ZIP_CODE=(By.CSS_SELECTOR,"#billing_postcode")
    PHONE= (By.CSS_SELECTOR,"#billing_phone")
    EMAIL = (By.CSS_SELECTOR,"#billing_email")
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR,"#place_order")


