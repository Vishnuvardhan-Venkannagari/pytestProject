from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_google():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("http://www.google.com")
    print(driver.title)
    assert driver.title == "Google"
    driver.quit()

def test_gmail():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("http://www.gmail.com")
    print(driver.title)
    assert driver.title == "Gmail"
    driver.quit()

def test_Instagram():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("http://www.instagram.com")
    print(driver.title)
    assert driver.title == "Instagram"
    driver.quit()

def test_facebook():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("http://www.facebook.com")
    print(driver.title)
    assert driver.title == "Facebook - log in or sign up"
    driver.quit()