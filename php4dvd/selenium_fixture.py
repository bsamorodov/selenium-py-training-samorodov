from selenium import webdriver
import pytest

@pytest.fixture
def app(request):
    driver = webdriver.Firefox(capabilities={'native_events':True})
    driver.implicitly_wait(1))
    request.addfinalizer(driver.quit)
    return Application(driver)
