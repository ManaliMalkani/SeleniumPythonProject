import pytest
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.base.DriverClass import WebDriverClass
import time


@pytest.fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = WebDriverClass()
    driver = driver1.getWebDriver("chrome")
    bp = BaseClass(driver)
    bp.launchWebPage("http://www.dummypoint.com/", "Selenium Template")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')


@pytest.fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
