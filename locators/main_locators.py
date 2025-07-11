from selenium.webdriver.common.by import By

CREATE_AD_BUTTON = (By.XPATH, '//button[contains(., "Разместить объявление")]')
LOGIN_MODAL = (By.CSS_SELECTOR, '.auth-modal')
MODAL_TITLE = (By.CSS_SELECTOR, '.modal-title')
LOGOUT_BUTTON = (By.XPATH, '//button[contains(., "Выйти")]')