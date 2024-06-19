from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from browser import Browser


class BasePage(Browser):

    #Actions

    def wait_for_element_presence(self,locator, seconds):
        # testez ca finish este afisat si adaug wait
        wait = WebDriverWait(self.driver, timeout=seconds)
        wait.until(expected_conditions.visibility_of_element_located(locator))
    def wait_for_elem(self, locator, seconds):
        wait = WebDriverWait(self.driver, timeout=seconds)
        wait.until(expected_conditions.presence_of_element_located(locator))

    def wait_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))


    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def type(self,locator, text):
        return self.find(locator).send_keys(text)

    def click(self, locator):
        return self.find(locator).click()


    #Validations
    def verify_page_url(self, expected):
        self.wait_url(expected)
        assert self.driver.current_url == expected, 'Error, URL is not the same'

    def verify_page_url_contains(self, expected):
        print(self.driver.current_url)
        assert expected in self.driver.current_url



    def verify_page_title(self, expected):
        assert self.driver.title == expected, 'Error, Title is not the same'



