Class Application(object):

    def __init__(sefl, driver):
        self.driver = driver

    def go_to_homepage(self):
        self.driver.get("http://hub.wart.ru/php4dvd/")

    def login(self, user):
        driver = self.driver
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(user.username)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(user.password)
        driver.find_element_by_id("submit").click()

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Log out").click()
        driver.switch_to_alert().accept()

    def is_element_present(driver,  how, what):
        try:
            driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True
