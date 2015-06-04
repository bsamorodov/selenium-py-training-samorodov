# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *


class Application(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_homepage(self):
        self.driver.get("http://hub.wart.ru/php4dvd/")

    def login(self, user):
        driver = self.driver
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(user.username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(user.password)
        driver.find_element_by_name("submit").click()

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Log out").click()
        driver.switch_to_alert().accept()

#    def is_logged_in(self):
#        driver = self.driver
#        try:
#            self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "nav")))
#            return True
#        except WebDriverException:
#            return False

    def is_not_logged_in(self):
        driver = self.driver
        try:
            self.wait.until(presence_of_element_located((By.ID, "loginform")))
            return True
        except WebDriverException:
            return False

    def add_film_with_all_needed_fields(self):
        driver = self.driver
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        form = driver.find_element_by_id("updateform")
        form.find_element_by_name("name").clear()
        form.find_element_by_name("name").send_keys("Test film")
        form.find_element_by_name("year").clear()
        form.find_element_by_name("year").send_keys("1999")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()

    def is_film_inserted(self):
        driver = self.driver
        try:
            self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "img[alt=\"Own\"]")))
            return True
        except WebDriverException:
            return False

    def add_film_withot_year_field(self):
        driver = self.driver
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        form = driver.find_element_by_id("updateform")
        form.find_element_by_name("name").clear()
        form.find_element_by_name("name").send_keys("Test film")
        form.find_element_by_name("year").clear()
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()

    def is_save_present(self):
        driver = self.driver
        try:
            self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "img[alt=\"Save\"]")))
            return True
        except WebDriverException:
            return False

    def delete_film(self):
        driver = self.driver
        driver.find_element_by_css_selector(u"img[alt=\"Солнце\"]").click()
        driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
        assertRegexpMatches(close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")

    def is_home_page(self):
        driver = self.driver
        try:
            self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "img[alt=\"Add movie\"]")))
            return True
        except WebDriverException:
            return False
