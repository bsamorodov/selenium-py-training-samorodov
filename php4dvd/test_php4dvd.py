# -*- coding: utf-8 -*-
from model.user import User
from model.keys import Keys
from model.names import Name
from model.id import Id
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium_fixture import app

def test_addfilm_without_year_field_set(app):
    app.go_to_homepage()
    app.login(User.Admin())
    app.driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
    form = app.driver.find_element_by_id(Id.UpdateForm)
    form.find_element_by_name(Name.name).clear()
    form.find_element_by_name(Name.name).send_keys(Keys.TestFilm)
    form.find_element_by_name(Name.year).clear()
    app.driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
    assert app.is_element_present(By.CSS_SELECTOR, "img[alt=\"Save\"]") == True
    app.logout()

#def test_addfilm_with_all_required_fields_set(app):
#    app.go_to_homepage()
#    app.login(User.Admin())
#    app.driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
#    form = app.driver.find_element_by_id(Id.UpdateForm)
#    form.find_element_by_name(Name.name).clear()
#    form.find_element_by_name(Name.name).send_keys(Keys.TestFilm)
#    form.find_element_by_name(Name.name).clear()
#    form.find_element_by_name(Name.name).send_keys("1999")
#    app.driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
#    assert app.is_element_present(By.CSS_SELECTOR, "img[alt=\"Own\"]") == True
#    app.logout()

#def test_deletefilm(app):
#    app.go_to_homepage()
#    app.login(User.Admin())
#    app.driver.find_element_by_css_selector(u"img[alt=\"Солнце\"]").click()
#    app.driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
#    assertRegexpMatches(close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")
#    assertRegexpMatches(close_alert_and_get_its_text(), r"^Are you sure you want to log out[\s\S]$")
#    app.logout()

#def test_search_existing_film(app):
#    app.go_to_homepage()
#    app.login(User.Admin())
#    app.driver.find_element_by_id(Id.Q.clear()
#    app.driver.find_element_by_id(Id.Q).send_keys(u"вос")
#    app.driver.find_element_by_id(Id.Q).send_keys(Keys.RETURN)
#    wait = WebDriverWait(app.driver, 10)
#    wait.until(invisibility_of_element_located((By.ID, "loading")))
#    results = app.driver.find_element_by_id(Id.Results)
#    if not results.find_elements_by_class_name("title"):
#        fail("Movie not found")
#    app.logout()

#def test_search_film_not_present(app):
#    app.go_to_homepage()
#    app.login(User.Admin())
#    app.driver.find_element_by_id(Id.Q).send_keys(Keys.TestFilm)
#    app.driver.find_element_by_id(Id.Q).send_keys(Keys.RETURN)
#    wait = WebDriverWait(app.driver, 10)
#    wait.until(invisibility_of_element_located((By.ID, "loading")))
#    results = app.driver.find_element_by_id(Id.Results)
#    if not app.is_element_present(By.CLASS_NAME, "content"):
#        fail("Movie found")
#    app.logout()
