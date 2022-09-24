import pdb
import time

import pytest

from src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    def test_login_none_existing_user(self):
        my_account = MyAccountSignedOut(self.driver)

        my_account.go_to_my_account()
        my_account.input_login_username("Bojan Stanisin")
        my_account.input_login_password("123456789")
        my_account.click_login_button()
        expected_error= "Error: The username Bojan Stanisin is not registered on this site. If you are unsure of your username, try your email address instead."
        my_account.wait_until_error_is_displayed(expected_error)

