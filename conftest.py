import pytest
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 10)

@pytest.fixture
def random_email():
    return f"test_{uuid.uuid4().hex[:8]}@example.com"

@pytest.fixture
def test_user():
    return {"email": "test@example.com", "password": "Test1234"}