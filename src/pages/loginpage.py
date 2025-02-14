from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):

    url = "https://the-internet.herokuapp.com/login"

    locators = {
        'user_name': ('XPATH', '//*[@id="username"]'),
        'password': ('XPATH', '//*[@id="password"]'),
        'header': ('XPATH', '//h2[text()="Login Page"]'),
        'login_btn': ('CSS', 'button[type="submit"]'),
        'invalid_login_label': (
            'XPATH', '//div[contains(text(), "Your username is invalid!")]'),
        'valid_login_label': (
            'XPATH', '//div[contains(text(), "You logged into a secure area!")]')
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

    def type_username(self, username: str):
        self.user_name.set_text(username)
        self.logger.info(f"username typed: {username}")

    def type_password(self, password: str):
        self.password.set_text(password)
        self.logger.info(f"password typed: {password}")

    def click_login(self):
        self.login_btn.click()
        self.logger.info("login button clicked")

    def verify_invalid_login(self):
        self.invalid_login_label.visibility_of_element_located()
        self.logger.info("invalid login label is visible")

    def verify_valid_login(self):
        self.valid_login_label.visibility_of_element_located()
        self.logger.info("valid login label is visible")

