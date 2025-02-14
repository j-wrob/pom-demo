from seleniumpagefactory.Pagefactory import PageFactory

class DropdownPage(PageFactory):

    url = "https://the-internet.herokuapp.com/dropdown"

    locators = {
        'header': ('XPATH', '//h3[text()="Dropdown List"]'),
        'dropdown': ('ID', 'dropdown')
    }

    def __init__(self, driver, test_logger):
        super().__init__()
        self.driver = driver
        self.logger = test_logger



    def get_url(self):
        self.logger.info(f"Getting url: {self.url}")
        self.driver.get(self.url)
        self.logger.info(f"Checking visibility of header")
        self.header.visibility_of_element_located()
        self.logger.info(f"URL: {self.url} loaded successfully")

    # using PageFactory method
    def select_from_dropdown_by_value(self, value):
        self.logger.info(f"Selecting element by value: {value}")
        self.dropdown.select_element_by_value(value)
        self.logger.info("Element from dropdown selected successfully")

    # pure selenium method
    # def select_from_dropdown_by_value(self, value):
    #     WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "dropdown")))
    #     dropdown = self.driver.find_element(By.ID, "dropdown")
    #     select = Select(dropdown)
    #     select.select_by_value(value)