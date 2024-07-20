from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

driver = None

@pytest.fixture(scope="class")
def init_driver(request):
    service = Service(ChromeDriverManager().install())
    
    # ch_dr = webdriver.Chrome(service=service)
    # request.cls.driver = ch_dr
    "Here above we can also use create var first and install driver to and assign it to request.cls.driver"
    
    request.cls.driver = webdriver.Chrome(service=service)
    #Above we are using a request.cls which sets the class variale explcitly
    request.cls.driver.implicitly_wait(10)
    yield 

    #ch_dr.close() 
    "In above if we use var we have to close connection with var object"
    
    request.cls.driver.close()


@pytest.mark.usefixtures("init_driver") 
class Base_Chrome_Test:
    pass

class TestClsChrome(Base_Chrome_Test):
    def test_google2(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"