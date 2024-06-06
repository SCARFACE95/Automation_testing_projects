# Asta este un fisier in care se definesc elementele comune ale unei pagini web:
# de exemplu oriunde ai naviga mereu sunt afisate elementele gen cauta, Login, Register, Categorii etc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser import Browser


class BasePage(Browser):

    # se pot pune locatori si metode ajutatoare pe care sa le folosim apoi in pagina

    #pun locator pt element search (de text)
    SEARCH_INPUT = (By.ID, "small-searchterms")
    #Si butonul de search
    SEARCH_BUTTON = (By.CLASS_NAME, "search-box-button")


    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self,locator):
        return self.driver.find_elements(*locator)


    def type(self, locator, text):
        return self.find(locator).send_keys(text)

    def click(self, locator):
        self.find(locator).click()

    def enter_search_term(self, text):
        self.type(self.SEARCH_INPUT, text)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)

    def verify_page_url(self, expected_url):
        assert self.driver.current_url == expected_url, "Error, Unexpected page URL"

    def verify_page_url_contains_text(self, text):
        assert text in self.driver.current_url, "Error, text not present in url"

    #de implementat dropdown
    def select_dropdown_text(self, locator, text):
        dropdown = Select(self.find(locator))
        dropdown.select_by_visible_text(text)




