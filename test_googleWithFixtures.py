from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = None

@pytest.fixture(scope="module")
def init_driver():
    global driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.delete_all_cookies
    driver.get("http://www.google.com")
    
    yield  # it makes to execute the code till here untill the test cases executed and after that it executes code below it
    driver.quit()

def test_google(init_driver):
    assert driver.title == "Google"

@pytest.mark.usefixtures("init_driver") # in this case we dont need to pass the fixture as a parameter as we are using in the annotation
def test_google2():
    assert driver.title == "Google"