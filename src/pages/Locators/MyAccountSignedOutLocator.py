from selenium.webdriver.common.by import By


class MyAccountSignedOutLocator:
    LOGIN_USER_NAME = (By.CSS_SELECTOR, "#username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")

    ERROR_MESSAGE_NON_EXISTING_USER =(By.CSS_SELECTOR,"#content > div > div.woocommerce > ul > li")