from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = None

@pytest.fixture(params=["chrome", "safari"],scope="class")
def init_driver(request):
    if request.param == "chrome":
        service = Service(ChromeDriverManager().install())
        dr = webdriver.Chrome(service=service)
    if request.param == "safari":
        dr = webdriver.Safari()
    request.cls.driver = dr
    request.cls.driver.implicitly_wait(10)
    yield 
    dr.close() 


@pytest.mark.usefixtures("init_driver") 
class BaseMultiDriver_Test:
    pass

class TestMultiDriver(BaseMultiDriver_Test):
    def test_google2(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"