from src.SeleniumExtended import SeleniumExtended
from src.pages.Locators.CartPageLocator import CartPageLocator


class CartPage(CartPageLocator):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def click_on_cart(self):
        self.sl.wait_and_click(self.CLICKING_CART)

    def input_coupon(self,coupon_code):
        self.sl.wait_and_input_text(self.COUPON_FIELD,coupon_code)

    def click_apply_coupon(self):
        self.sl.wait_and_click(self.APPLY_COUPON)

    def click_on_proceed_to_checkout(self):
        self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT)




