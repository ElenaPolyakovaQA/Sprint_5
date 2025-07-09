import pytest
from pages.auth_page import AuthPage
from pages.main_page import MainPage

class TestAuth:
    def test_successful_login(self, browser, wait, test_user):
        auth_page = AuthPage(browser, wait)
        main_page = MainPage(browser, wait)
        
        auth_page.open_login_form()
        auth_page.login_user(test_user["email"], test_user["password"])
        assert main_page.is_user_logged_in()

    def test_logout(self, browser, wait, test_user):
        auth_page = AuthPage(browser, wait)
        main_page = MainPage(browser, wait)
        
        auth_page.open_login_form()
        auth_page.login_user(test_user["email"], test_user["password"])
        main_page.logout()
        assert main_page.is_login_button_displayed()