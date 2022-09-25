import pytest

@pytest.mark.usefixtures("init_driver")
class TestEndToEndCheckOutGuestUser:

    def test_end_to_end_checkout_guest_user(self):
        pass
        # go to homepage
        # add 1 item to cart
        # apply free coupon
        # select free shipping
        # click on place order
        # verify order is received
        # verify taht the order is recorded in database












