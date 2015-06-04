# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium_fixture import driver

def test_addfilm_without_year_field_set(app):
    app.go_to_homepage())
    app.login(User.Admin())
    app.driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
    form = app.driver.find_element_by_id("updateform")
    form.find_element_by_name("name").clear()
    form.find_element_by_name("name").send_keys("Test film")
    form.find_element_by_name("year").clear()
    app.driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
    assert app.is_element_present(By.CSS_SELECTOR, "img[alt=\"Save\"]") == True
    app.logout()

def test_addfilm_with_all_required_fields_set(app):
    app.go_to_homepage())
    app.login(User.Admin())
    app.driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
    form = app.driver.find_element_by_id("updateform")
    form.find_element_by_name("name").clear()
    form.find_element_by_name("name").send_keys("Test film")
    form.find_element_by_name("year").clear()
    form.find_element_by_name("year").send_keys("1999")
    app.driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
    assert app.is_element_present(By.CSS_SELECTOR, "img[alt=\"Own\"]") == True
    app.logout()

def test_deletefilm(app):
    app.go_to_homepage())
    app.login(User.Admin())
    app.driver.find_element_by_css_selector(u"img[alt=\"Солнце\"]").click()
    app.driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
    assertRegexpMatches(close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")
    app.driver.find_element_by_link_text("Home").click()
    app.driver.find_element_by_link_text("Log out").click()
    assertRegexpMatches(close_alert_and_get_its_text(), r"^Are you sure you want to log out[\s\S]$")
    app.logout()

def test_search_existing_film(app):
    app.go_to_homepage())
    app.login(User.Admin())
    app.driver.find_element_by_id("q").clear()
    app.driver.find_element_by_id("q").send_keys(u"вос")
    app.driver.find_element_by_id("q").send_keys(Keys.RETURN)
    wait = WebDriverWait(app.driver, 10)
    wait.until(invisibility_of_element_located((By.ID, "loading")))
    results = app.driver.find_element_by_id("results")
    if not results.find_elements_by_class_name("title"):
        fail("Movie not found")
    app.logout()

def test_search_film_not_present(app):
    app.go_to_homepage())
    app.login(User.Admin())
    app.driver.find_element_by_id("q").send_keys("Test film")
    app.driver.find_element_by_id("q").send_keys(Keys.RETURN)
    wait = WebDriverWait(app.driver, 10)
    wait.until(invisibility_of_element_located((By.ID, "loading")))
    results = app.driver.find_element_by_id("results")
    if not app.is_element_present(By.CLASS_NAME, "content"):
        fail("Movie found")
    app.logout()
