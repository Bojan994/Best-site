from src.pages.Locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.SeleniumExtended import SeleniumExtended
from src.helpers.config_helpers import get_base_url


class MyAccountSignedOut(MyAccountSignedOutLocator):
    endpoint = "/my-account"

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        self.sl.wait_and_click(self.LOGIN_BUTTON)

    def wait_until_error_is_displayed(self,expected_error):self.sl.wait_until_element_contains_text(self.ERROR_MESSAGE_NON_EXISTING_USER,expected_error)

    def input_register_email(self,email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL,email)

    def input_register_password(self,password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD,password)

    def click_register_button(self):
        self.sl.wait_and_click(self.REGISTER_BUTTON)