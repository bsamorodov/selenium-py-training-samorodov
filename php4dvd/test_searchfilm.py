# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.by import By
import unittest


class searchFilm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(capabilities={'native_events':True})
        self.driver.implicitly_wait(10)
        self.base_url = "http://hub.wart.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.get(self.base_url + "php4dvd/")
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("admin")
        self.driver.find_element_by_name("submit").click()

    def test_search_existing_film(self):
        driver = self.driver
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys(u"вос")
        driver.find_element_by_id("q").send_keys(Keys.RETURN)
        wait = WebDriverWait(driver, 10)
        results = wait.until(presence_of_element_located((By.ID, "results")))
        if not results.find_elements_by_class_name("title"):
            self.fail("Movie not found")

    def test_search_film_not_present(self):
        driver = self.driver
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys("Test film")
        driver.find_element_by_id("q").send_keys(Keys.RETURN)
        wait = WebDriverWait(driver, 10)
        results = wait.until(presence_of_element_located((By.ID, "results")))
        assert driver.find_element_by_class_name("content"
          ).get_attribute("textContent") == "No movies where found."

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.find_element_by_link_text("Log out").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to log out[\s\S]$")
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
