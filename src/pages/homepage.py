from seleniumpagefactory.Pagefactory import PageFactory
import logging

logger = logging.getLogger("HomePageLogger")

class HomePage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    url = "https://the-internet.herokuapp.com"

    locators = {
        'header': ('XPATH', '//h1[text()="Welcome to the-internet"]')
    }

    def get_url(self):
        self.driver.get(self.url)
        self.header.visibility_of_element_located()
        logger.info("HomePage URL get - successfully")
