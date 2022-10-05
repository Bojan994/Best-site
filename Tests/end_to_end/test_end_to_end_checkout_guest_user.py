import pdb
import time
from src.configs.Generic_configs import GenericConfigs

import pytest
from src.pages.HomePage import HomePage
from src.pages.CartPage import CartPage
from src.pages.CheckoutPage import CheckoutPage
from src.pages.OrederReceivedPage import OrderReceivedPage


@pytest.mark.usefixtures("init_driver")
class TestEndToEndCheckOutGuestUser:
    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):
        cart_page = CartPage(self.driver)
        checkout_page=CheckoutPage(self.driver)
        order_received_page=OrderReceivedPage(self.driver)
        # go to homepage
        home_page = HomePage(self.driver)
        home_page.go_to_homepage()
        # add 1 item to cart
        home_page.click_add_to_cart_button()
        time.sleep(3)
        # go to cart
        cart_page.click_on_cart()
        # apply free coupon
        coupon_code = GenericConfigs.FREE_COUPON
        cart_page.input_coupon(coupon_code)
        cart_page.click_apply_coupon()
        # click on checkout
        cart_page.click_on_proceed_to_checkout()
        # fill the form
        checkout_page.input_first_name()
        checkout_page.input_last_name()
        checkout_page.input_street_address()
        checkout_page.input_city()
        checkout_page.input_zip_code()
        checkout_page.input_phone()
        checkout_page.input_email()
        # click on place order
        checkout_page.click_place_order()

        # verify order is received
        order_received_page.verify_order_received_page_loaded()



        # verify that the order is recorded in database
