from src.pages.Locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.SeleniumExtended import SeleniumExtended
from src.helpers.config_helpers import get_base_url


class MyAccountSignedOut(MyAccountSignedOutLocator):
    endpoint = "/my-account"

    def __init__(self, driver):
        self.driver = driver
        self.selenium_extended = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url =base_url + self.endpoint
        self.driver.get (my_account_url)

    def input_login_user_name(self, username):
        self.selenium_extended.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.selenium_extended.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        self.selenium_extended.wait_and_click(self.LOGIN_BUTTON)
