from selenium.webdriver.common.by import By
from browser import Browser

class HomePageLocator(object):
    # Home Page Locators

    HEADER_TEXT = (By.XPATH, "//h1")
    SEARCH_FIELD = (By.ID, "term")
    SUBMIT_BUTTON = (By.ID, "submit")


class HomePage(Browser):
    # Home Page Actions
    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)