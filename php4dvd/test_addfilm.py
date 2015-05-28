# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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

    def test_addfilm(self):
        driver = self.driver

        # try to insert a film without a required field "year"
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        form = driver.find_element_by_id("updateform")
        form.find_element_by_name("name").clear()
        form.find_element_by_name("name").send_keys("Test film")
        form.find_element_by_name("year").clear()
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()

        # go home and test if a test film is present
        driver.find_element_by_link_text("Home").click()
        if driver.find_elements_by_css_selector("div.nocover[alt=\"Test film\"]"):
            self.fail("Test film was found")

        # insert a film  from imbd database and download the cover
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_id("imdbsearch").clear()
        driver.find_element_by_id("imdbsearch").send_keys("sun")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text(u"Солнце").click()
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(u"Фильм Сокурова А.Н. Император Хирохито, Вторая Мировая война.")
        driver.find_element_by_name("aka").clear()
        driver.find_element_by_name("aka").send_keys(u"The Sun")
        driver.find_element_by_id("own_no").click()
        driver.find_element_by_id("seen_no").click()
        driver.find_element_by_id("cover").send_keys("/home/bsam/selenium-py-training-samorodov/php4dvd/img/the_sun.jpg")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()

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
