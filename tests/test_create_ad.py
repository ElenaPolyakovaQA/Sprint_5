import pytest
import uuid
from pages.main_page import MainPage
from pages.profile_page import ProfilePage

class TestCreateAd:
    def test_create_ad_unauthorized(self, browser, wait):
        main_page = MainPage(browser, wait)
        main_page.open_create_ad_form()
        
        assert main_page.is_login_modal_displayed()
        assert "авторизуйтесь" in main_page.get_modal_title()

    def test_create_ad_authorized(self, browser, wait, authorized_user):
        from pages.main_page import MainPage
        from pages.profile_page import ProfilePage
        
        main_page = MainPage(browser, wait)
        profile_page = ProfilePage(browser, wait)
        
        main_page.open_create_ad_form()
        
        ad_title = f"Test Ad {uuid.uuid4().hex[:6]}"
        profile_page.create_ad(
            title=ad_title,
            description="Test description",
            price="1000",
            category="Электроника",
            city="Москва",
            condition="new"
        )
        
        assert profile_page.is_ad_displayed(ad_title)