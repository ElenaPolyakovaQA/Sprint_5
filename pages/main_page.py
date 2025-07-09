from locators.main_locators import *

class MainPage:
    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait

    def is_user_logged_in(self):
        avatar_visible = self.wait.until(lambda d: d.find_element(*USER_AVATAR).is_displayed())
        username_visible = self.wait.until(lambda d: d.find_element(*USERNAME).is_displayed())
        return avatar_visible and username_visible

    def logout(self):
        self.browser.find_element(*LOGOUT_BUTTON).click()
        self.wait.until(lambda d: d.find_element(*LOGIN_BUTTON).is_displayed())

    def is_login_button_displayed(self):
        return self.wait.until(lambda d: d.find_element(*LOGIN_BUTTON).is_displayed())

    def open_create_ad_form(self):
        self.browser.find_element(*CREATE_AD_BUTTON).click()

    def is_login_modal_displayed(self):
        return self.wait.until(lambda d: d.find_element(*LOGIN_MODAL).is_displayed())