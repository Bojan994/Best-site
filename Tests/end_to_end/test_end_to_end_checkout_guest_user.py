import pdb
import time
from src.configs.Generic_configs import GenericConfigs

import pytest
from src.pages.HomePage import HomePage
from src.pages.CartPage import CartPage


@pytest.mark.usefixtures("init_driver")
class TestEndToEndCheckOutGuestUser:
    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):
        cart_page = CartPage(self.driver)
        # go to homepage
        home_page = HomePage(self.driver)
        home_page.go_to_homepage()
        # add 1 item to cart
        home_page.click_add_to_cart_button()
        # go to cart
        cart_page.click_on_cart()
        # apply free coupon
        coupon_code = GenericConfigs.FREE_COUPON
        cart_page.input_coupon(coupon_code)
        cart_page.click_apply_coupon()
        # click on checkout
        cart_page.click_on_proceed_to_checkout()
        pdb.set_trace()
        # select free shipping
        # click on place order
        # verify order is received
        # verify that the order is recorded in database
