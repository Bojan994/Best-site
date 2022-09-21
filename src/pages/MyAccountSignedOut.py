from src.pages.Locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MyAccountSignedOut(MyAccountSignedOutLocator):

    def __init__(self, driver):
        self.driver = driver

    def go_to_my_account(self):
        pass

    def input_login_user_name(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_USER_NAME)).send_keys(username)

    def input_login_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_PASSWORD)).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_BUTTON)).click()
