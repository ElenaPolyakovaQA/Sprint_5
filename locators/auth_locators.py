from selenium.webdriver.common.by import By

LOGIN_BUTTON = (By.XPATH, '//button[contains(., "Вход и регистрация")]')
REGISTER_LINK = (By.XPATH, '//a[contains(., "Нет аккаунта")]')
EMAIL_INPUT = (By.CSS_SELECTOR, 'input[name="email"]')
PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="password"]')
REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[name="repeat_password"]')
SUBMIT_BUTTON = (By.XPATH, '//button[contains(., "Создать аккаунт") or contains(., "Войти")]')
ERROR_MESSAGE = (By.CSS_SELECTOR, '.error-message')
ERROR_FIELD = (By.CSS_SELECTOR, '.error-field')
AVATAR = (By.CSS_SELECTOR, '.user-avatar')
USERNAME = (By.CSS_SELECTOR, '.user-name')