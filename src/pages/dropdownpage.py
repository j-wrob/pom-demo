from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support.select import Select
import logging

logger = logging.getLogger("DropdownPageLogger")

class DropdownPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    url = "https://the-internet.herokuapp.com/dropdown"

    locators = {
        'header': ('XPATH', '//h3[text()="Dropdown List"]'),
        'dropdown': ('ID', 'dropdown')
    }

    def get_url(self):
        self.driver.get(self.url)
        self.header.visibility_of_element_located()
        logger.info("DropdownPage URL get - successfully")

    def select_element_by_value(self, value):
        self.dropdown.select_element_by_value(value)
        logger.info("Element from dropdown selected successfully")