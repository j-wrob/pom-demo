from seleniumpagefactory.Pagefactory import PageFactory

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    # using PageFactory method
    def select_from_dropdown_by_value(self, value):
        self.dropdown.select_element_by_value(value)
        logger.info("Element from dropdown selected successfully")

    # pure selenium method
    # def select_from_dropdown_by_value(self, value):
    #     WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "dropdown")))
    #     dropdown = self.driver.find_element(By.ID, "dropdown")
    #     select = Select(dropdown)
    #     select.select_by_value(value)