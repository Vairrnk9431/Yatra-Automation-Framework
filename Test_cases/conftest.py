from sys import executable
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



@pytest.fixture(autouse=True)
def setup(request,browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver=webdriver.Firefox()
    elif browser == "edge":
        driver=webdriver.Edge()        
    driver.get("https://www.yatra.com")
    driver.maximize_window()
    request.cls.driver=driver
    yield driver
    driver.quit()



def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class",autouse=True)
def browser(request):
    return request.config.getoption("--browser")




