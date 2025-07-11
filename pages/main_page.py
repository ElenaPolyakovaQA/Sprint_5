from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.main_locators import *

class MainPage:
    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait

    def open_create_ad_form(self):
        self.wait.until(EC.element_to_be_clickable(CREATE_AD_BUTTON)).click()

    def is_login_modal_displayed(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(LOGIN_MODAL)).is_displayed()
        except TimeoutException:
            return False

    def is_login_button_displayed(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(LOGIN_BUTTON)).is_displayed()
        except TimeoutException:
            return False

    def get_modal_title(self):
        return self.wait.until(EC.visibility_of_element_located(MODAL_TITLE)).text