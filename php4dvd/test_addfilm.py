# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import unittest


class AddFilm(unittest.TestCase):
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

    def test_addfilm_without_year_field_set(self):
        driver = self.driver
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        form = driver.find_element_by_id("updateform")
        form.find_element_by_name("name").clear()
        form.find_element_by_name("name").send_keys("Test film")
        form.find_element_by_name("year").clear()
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        assert self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Save\"]") == True

    def test_addfilm_with_all_required_fields_set(self):
        driver = self.driver
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        form = driver.find_element_by_id("updateform")
        form.find_element_by_name("name").clear()
        form.find_element_by_name("name").send_keys("Test film")
        form.find_element_by_name("year").clear()
        form.find_element_by_name("year").send_keys("1999")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        assert self.is_element_present(By.CSS_SELECTOR, "img[alt=\"Own\"]") == True

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
