import pytest
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    
    yield driver
    driver.quit()

@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, timeout=15)

@pytest.fixture
def random_email():
    return f"user_{uuid.uuid4().hex[:8]}@example.com"

@pytest.fixture
def test_user():
    return {
        "email": "test_user@example.com",
        "password": "TestPass123!",
        "name": "Test User"
    }

@pytest.fixture
def authorized_user(browser, wait, test_user):
    from pages.auth_page import AuthPage
    auth_page = AuthPage(browser, wait)
    auth_page.open_login_form()
    auth_page.login_user(test_user["email"], test_user["password"])
    yield
    auth_page.logout()