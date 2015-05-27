# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import unittest


class searchFilm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://hub.wart.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_searchfilm(self):
        driver = self.driver
        driver.get(self.base_url + "php4dvd/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()

        # search a film which does present
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys(u"Вос")
        driver.find_element_by_id("q").send_keys(Keys.RETURN)
        results = driver.find_element_by_id("results")
        if not results.find_elements_by_class_name("title"):
            self.fail("Movie not found")

        # search a film which does not present
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys("Test film")
        driver.find_element_by_id("q").send_keys(Keys.RETURN)
        results = driver.find_element_by_id("results")
        if not results.find_elements_by_class_name("content"):
            self.fail("Movies found")

        # finish our tests
        driver.find_element_by_link_text("Log out").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to log out[\s\S]$")


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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
