from model.user import User
from model.id import Id
from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import app


def test_addfilm_with_all_required_fields_set(app):
    app.go_to_homepage()
    app.login(User.Admin())
    app.add_film_with_all_needed_fields()
    assert app.is_film_inserted()
    app.logout()

def test_addfilm_with_one_required_field_absent(app):
    app.go_to_homepage()
    app.login(User.Admin())
    app.add_film_withot_year_field()
    assert app.is_save_present()
    app.logout()

def test_delete_film(app):
    app.go_to_homepage()
    app.login(User.Admin())
    app.delete_film()
    assert app.is_home_page()
    app.logout()

