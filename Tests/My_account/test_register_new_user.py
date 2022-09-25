import pdb
from src.helpers.generic_helpers import generate_random_email
import pytest
from src.pages.MyAccountSignedOut import MyAccountSignedOut
from src.pages.MyAccountSignedIn import MyAccountSignedIn


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:
    @pytest.mark.tcid13
    def test_register_new_user(self):
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account_signed_in = MyAccountSignedIn(self.driver)

        random_email = generate_random_email()
        my_account.input_register_email(random_email["email"])
        my_account.input_register_password("whatareyoudoing993.")
        my_account.click_register_button()
        my_account_signed_in.verify_user_is_signed_in()

