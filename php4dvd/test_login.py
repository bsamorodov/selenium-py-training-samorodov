# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest


class Login(unittest.TestCase):
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

    def test_login(self):
        driver = self.driver
        driver.find_element_by_id("q")

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