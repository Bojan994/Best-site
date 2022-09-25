from src.SeleniumExtended import SeleniumExtended
from src.pages.Locators.MyAccountSignedInLocator import MyAccountSignedInLocator


class MyAccountSignedIn(MyAccountSignedInLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_user_is_signed_in(self):
        self.sl.wait_until_element_is_visible(self.LOGOUT_BUTTON)
