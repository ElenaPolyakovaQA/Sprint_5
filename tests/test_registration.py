import pytest
from pages.auth_page import AuthPage
from pages.main_page import MainPage

class TestRegistration:
    def test_successful_registration(self, browser, wait, random_email):
        auth_page = AuthPage(browser, wait)
        main_page = MainPage(browser, wait)
        
        auth_page.open_login_form()
        auth_page.go_to_registration()
        auth_page.register_user(random_email, "TestPass123!")
        
        assert main_page.is_user_logged_in()

    def test_invalid_email_registration(self, browser, wait):
        auth_page = AuthPage(browser, wait)
        
        auth_page.open_login_form()
        auth_page.go_to_registration()
        auth_page.register_user("invalid_email", "TestPass123!")
        
        assert auth_page.is_error_displayed()

    def test_existing_user_registration(self, browser, wait, test_user):
        auth_page = AuthPage(browser, wait)
        
        auth_page.open_login_form()
        auth_page.go_to_registration()
        auth_page.register_user(test_user["email"], test_user["password"])
        
        assert auth_page.is_error_displayed()