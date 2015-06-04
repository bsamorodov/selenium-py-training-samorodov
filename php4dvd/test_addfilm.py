# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium_fixture import driver

def test_addfilm_without_year_field_set(app):
    login(app.driver, User.Admin())
    app.driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
    form = app.driver.find_element_by_id("updateform")
    form.find_element_by_name("name").clear()
    form.find_element_by_name("name").send_keys("Test film")
    form.find_element_by_name("year").clear()
    app.driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
    assert is_element_present(By.CSS_SELECTOR, "img[alt=\"Save\"]") == True
    logout(app.driver))

def test_addfilm_with_all_required_fields_set(app):
    login(app.driver, User.Admin())
    app.driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
    form = app.driver.find_element_by_id("updateform")
    form.find_element_by_name("name").clear()
    form.find_element_by_name("name").send_keys("Test film")
    form.find_element_by_name("year").clear()
    form.find_element_by_name("year").send_keys("1999")
    app.driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
    assert is_element_present(By.CSS_SELECTOR, "img[alt=\"Own\"]") == True
    logout(app.driver))

def test_deletefilm(app):
    login(app.driver, User.Admin())
    app.driver.find_element_by_css_selector(u"img[alt=\"Солнце\"]").click()
    app.driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
    assertRegexpMatches(close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")
    app.driver.find_element_by_link_text("Home").click()
    app.driver.find_element_by_link_text("Log out").click()
    assertRegexpMatches(close_alert_and_get_its_text(), r"^Are you sure you want to log out[\s\S]$")
    logout(app.driver))

def test_search_existing_film(app):
    login(app.driver, User.Admin())
    app.driver.find_element_by_id("q").clear()
    app.driver.find_element_by_id("q").send_keys(u"вос")
    app.driver.find_element_by_id("q").send_keys(Keys.RETURN)
    wait = WebDriverWait(app.driver, 10)
    wait.until(invisibility_of_element_located((By.ID, "loading")))
    results = app.driver.find_element_by_id("results")
    if not results.find_elements_by_class_name("title"):
        fail("Movie not found")
    logout(app.driver))

def test_search_film_not_present(app):
    login(app.driver, User.Admin())
    app.driver.find_element_by_id("q").clear()
    app.driver.find_element_by_id("q").send_keys("Test film")
    app.driver.find_element_by_id("q").send_keys(Keys.RETURN)
    wait = WebDriverWait(app.driver, 10)
    wait.until(invisibility_of_element_located((By.ID, "loading")))
    results = app.driver.find_element_by_id("results")
    if not is_element_present(By.CLASS_NAME, "content"):
        fail("Movie found")
    logout(app.driver))

def login(driver, user):
    driver.get("http://hub.wart.ru/php4dvd/")
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(user.username)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(user.password)
    driver.find_element_by_id("submit").click()

def logout(driver):
    driver.find_element_by_link_text("Log out").click()
    driver.switch_to_alert().accept()

def is_element_present(driver,  how, what):
    try:
        driver.find_element(by=how, value=what)
    except NoSuchElementException, e:
        return False
    return True
