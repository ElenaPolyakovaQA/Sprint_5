from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from locators.profile_locators import *

class ProfilePage:
    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait

    def create_ad(self, title, description, price, category, city, condition):
        self.browser.find_element(*AD_TITLE).send_keys(title)
        self.browser.find_element(*AD_DESCRIPTION).send_keys(description)
        self.browser.find_element(*AD_PRICE).send_keys(price)
        
        Select(self.browser.find_element(*AD_CATEGORY)).select_by_visible_text(category)
        Select(self.browser.find_element(*AD_CITY)).select_by_visible_text(city)
        
        if condition == "new":
            self.browser.find_element(*AD_CONDITION_NEW).click()
        else:
            self.browser.find_element(*AD_CONDITION_USED).click()
        
        self.browser.find_element(*PUBLISH_BUTTON).click()

    def is_ad_displayed(self, title):
        try:
            ads = self.wait.until(EC.visibility_of_all_elements_located(AD_ITEM))
            return any(title in ad.text for ad in ads)
        except TimeoutException:
            return False