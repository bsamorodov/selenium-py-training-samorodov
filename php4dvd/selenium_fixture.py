from model.application import Application
from selenium import webdriver
import pytest

@pytest.fixture(scope="module")
def app(request):
    driver = webdriver.Firefox(capabilities={'native_events':True})
    request.addfinalizer(driver.quit)
    return Application(driver)

