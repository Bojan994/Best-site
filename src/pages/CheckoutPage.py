from src.SeleniumExtended import SeleniumExtended
from src.pages.Locators.CheckoutPageLocator import CheckoutPageLocator
from src.helpers.generic_helpers import generate_random_email


class CheckoutPage(CheckoutPageLocator):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def input_first_name(self, first_name="Bojan"):
        self.sl.wait_and_input_text(self.FIRST_NAME, first_name)

    def input_last_name(self, last_name="Stanisin"):
        self.sl.wait_and_input_text(self.LAST_NAME, last_name)

    def input_street_address(self, street_address="Main street 23"):
        self.sl.wait_and_input_text(self.STREET_ADDRESS, street_address)

    def input_city(self, city="Los Angeles"):
        self.sl.wait_and_input_text(self.CITY, city)

    def input_zip_code(self, zip="21500"):
        self.sl.wait_and_input_text(self.ZIP_CODE, zip)

    def input_phone(self, phone="0649992344"):
        self.sl.wait_and_input_text(self.PHONE, phone)

    def input_email(self, email=None):
        if not email:
            rand_email = generate_random_email()
            email = rand_email["email"]
        self.sl.wait_and_input_text(self.EMAIL, email)

    def click_place_order(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BUTTON)
