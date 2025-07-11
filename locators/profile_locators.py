from selenium.webdriver.common.by import By

AD_TITLE = (By.CSS_SELECTOR, 'input[name="title"]')
AD_DESCRIPTION = (By.CSS_SELECTOR, 'textarea[name="description"]')
AD_PRICE = (By.CSS_SELECTOR, 'input[name="price"]')
AD_CATEGORY = (By.CSS_SELECTOR, 'select[name="category"]')
AD_CITY = (By.CSS_SELECTOR, 'select[name="city"]')
AD_CONDITION_NEW = (By.CSS_SELECTOR, 'input[value="new"]')
AD_CONDITION_USED = (By.CSS_SELECTOR, 'input[value="used"]')
PUBLISH_BUTTON = (By.XPATH, '//button[contains(., "Опубликовать")]')
MY_ADS_SECTION = (By.CSS_SELECTOR, '.my-ads')
AD_ITEM = (By.CSS_SELECTOR, '.ad-item')