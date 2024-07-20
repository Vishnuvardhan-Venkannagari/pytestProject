from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = None
def setup_module(module):
    global driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.delete_all_cookies
    driver.get("http://www.google.com")
    print(driver.title)
    
def terminate_module(module):
    driver.quit()

def test_google():
    assert driver.title == "Google"