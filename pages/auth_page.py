from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.auth_locators import *

class AuthPage:
    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait

    def open_login_form(self):
        self.wait.until(EC.element_to_be_clickable(LOGIN_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(EMAIL_INPUT))

    def go_to_registration(self):
        self.wait.until(EC.element_to_be_clickable(REGISTER_LINK)).click()
        self.wait.until(EC.visibility_of_element_located(REPEAT_PASSWORD_INPUT))

    def register_user(self, email, password):
        self.browser.find_element(*EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*REPEAT_PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*SUBMIT_BUTTON).click()

    def login_user(self, email, password):
        self.browser.find_element(*EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*SUBMIT_BUTTON).click()

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(LOGIN_BUTTON))

    def is_error_displayed(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(ERROR_MESSAGE)).is_displayed()
        except TimeoutException:
            return False

    def is_user_logged_in(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(AVATAR)).is_displayed()
        except TimeoutException:
            return False