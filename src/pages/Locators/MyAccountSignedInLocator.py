from selenium.webdriver.common.by import By


class MyAccountSignedInLocator:
    LOGOUT_BUTTON = (By.CSS_SELECTOR,
                     "#post-9 > div > div > nav > ul > li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a")
