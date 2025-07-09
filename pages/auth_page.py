from locators.auth_locators import *

class AuthPage:
    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait

    def open_login_form(self):
        self.browser.find_element(*LOGIN_BUTTON).click()
        self.wait.until(lambda d: d.find_element(*EMAIL_INPUT).is_displayed())

    def go_to_registration(self):
        self.browser.find_element(*REGISTER_LINK).click()
        self.wait.until(lambda d: d.find_element(*REPEAT_PASSWORD_INPUT).is_displayed())

    def register_user(self, email, password):
        self.browser.find_element(*EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*REPEAT_PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*SUBMIT_BUTTON).click()

    def login_user(self, email, password):
        self.browser.find_element(*EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*SUBMIT_BUTTON).click()

    def is_error_displayed(self):
        return self.wait.until(lambda d: d.find_element(*ERROR_MESSAGE).is_displayed())