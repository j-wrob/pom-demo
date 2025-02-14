from seleniumpagefactory.Pagefactory import PageFactory

class HomePage(PageFactory):

    url = "https://the-internet.herokuapp.com"

    def __init__(self, driver, test_logger):
        super().__init__()
        self.driver = driver
        self.logger = test_logger

    locators = {
        'header': ('XPATH', '//h1[text()="Welcome to the-internet"]')
    }

    def get_url(self):
        self.logger.info(f"Getting url: {self.url}")
        self.driver.get(self.url)
        self.logger.info(f"Checking visibility of header")
        self.header.visibility_of_element_located()
        self.logger.info(f"URL: {self.url} loaded successfully")