from selenium.webdriver.support.ui import Select
from locators.profile_locators import *

class ProfilePage:
    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait

    def create_ad(self, title, description, price, category, city, condition):
        self.browser.find_element(*AD_TITLE_INPUT).send_keys(title)
        self.browser.find_element(*AD_DESCRIPTION_INPUT).send_keys(description)
        self.browser.find_element(*AD_PRICE_INPUT).send_keys(price)
        
        Select(self.browser.find_element(*AD_CATEGORY_DROPDOWN)).select_by_visible_text(category)
        Select(self.browser.find_element(*AD_CITY_DROPDOWN)).select_by_visible_text(city)
        
        if condition == "new":
            self.browser.find_element(*AD_CONDITION_RADIO_NEW).click()
        else:
            self.browser.find_element(*AD_CONDITION_RADIO_USED).click()
        
        self.browser.find_element(*PUBLISH_BUTTON).click()
        self.wait.until(lambda d: d.find_element(*MY_ADS_SECTION).is_displayed())

    def is_ad_displayed(self, title):
        ads = self.wait.until(lambda d: d.find_elements(*AD_ITEM))
        return any(title in ad.text for ad in ads)