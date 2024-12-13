from seleniumpagefactory.Pagefactory import PageFactory

class LoginPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    url = "https://the-internet.herokuapp.com/login"

    locators = {
        'user_name': ('XPATH', '//*[@id="username"]'),
        'password': ('XPATH', '//*[@id="password"]'),
        'login_btn': ('CSS', 'button[type="submit"]'),
        'invalid_login_label': (
            'XPATH', '//div[contains(text(), "Your username is invalid!")]'),
        'valid_login_label': (
            'XPATH', '//div[contains(text(), "You logged into a secure area!")]')
    }

    def get_url(self):
        self.driver.get(self.url)

    def select_username(self, username: str):
        self.user_name.set_text(username)

    def select_password(self, password: str):
        self.password.set_text(password)

    def click_login(self):
        self.login_btn.click()

    def verify_invalid_login(self):
        self.invalid_login_label.visibility_of_element_located()

    def verify_valid_login(self):
        self.valid_login_label.visibility_of_element_located()
