import pytest
from src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    def test_login_none_existing_user(self):
        my_account = MyAccountSignedOut(self.driver)
       #go to my account
        my_account.go_to_my_account()
       #type username
        my_account.input_login_user_name("Bojan")
       # type password
        my_account.input_login_password("abcd1234")
       #click login
        my_account.click_login_button()

       #verify error message

