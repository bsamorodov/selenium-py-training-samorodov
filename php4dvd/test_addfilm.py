# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium_fixture import driver

def test_addfilm_without_year_field_set(driver):
    driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
    form = driver.find_element_by_id("updateform")
    form.find_element_by_name("name").clear()
    form.find_element_by_name("name").send_keys("Test film")
    form.find_element_by_name("year").clear()
    driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
    assert is_element_present(By.CSS_SELECTOR, "img[alt=\"Save\"]") == True

def test_addfilm_with_all_required_fields_set(driver):
    driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
    form = driver.find_element_by_id("updateform")
    form.find_element_by_name("name").clear()
    form.find_element_by_name("name").send_keys("Test film")
    form.find_element_by_name("year").clear()
    form.find_element_by_name("year").send_keys("1999")
    driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
    assert is_element_present(By.CSS_SELECTOR, "img[alt=\"Own\"]") == True

def test_deletefilm(driver):
    driver.find_element_by_css_selector(u"img[alt=\"Солнце\"]").click()
    driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
    assertRegexpMatches(close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")
    driver.find_element_by_link_text("Home").click()
    driver.find_element_by_link_text("Log out").click()
    assertRegexpMatches(close_alert_and_get_its_text(), r"^Are you sure you want to log out[\s\S]$")

def test_search_existing_film(driver):
    driver.find_element_by_id("q").clear()
    driver.find_element_by_id("q").send_keys(u"вос")
    driver.find_element_by_id("q").send_keys(Keys.RETURN)
    wait = WebDriverWait(driver, 10)
    wait.until(invisibility_of_element_located((By.ID, "loading")))
    results = driver.find_element_by_id("results")
    if not results.find_elements_by_class_name("title"):
        fail("Movie not found")

def test_search_film_not_present(driver):
    driver.find_element_by_id("q").clear()
    driver.find_element_by_id("q").send_keys("Test film")
    driver.find_element_by_id("q").send_keys(Keys.RETURN)
    wait = WebDriverWait(driver, 10)
    wait.until(invisibility_of_element_located((By.ID, "loading")))
    results = driver.find_element_by_id("results")
    if not is_element_present(By.CLASS_NAME, "content"):
        fail("Movie found")


def is_element_present(driver,  how, what):
    try:
        driver.find_element(by=how, value=what)
    except NoSuchElementException, e:
        return False
    return True
