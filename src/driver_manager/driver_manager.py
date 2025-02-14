from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.safari.service import Service as SafariService


from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions



class DriverManager:
    """
    DriverManager class
    """

    def __init__(self, browser):
        self.browser = browser
        self.driver = None

    def get_driver(self):
        """
        Reads browser type and returns proper driver instance
        """

        if self.browser.lower() == 'chrome':
            opt = ChromeOptions()
            serv = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome

        elif self.browser.lower() == 'firefox':
            opt = FirefoxOptions()
            serv = FirefoxService(GeckoDriverManager().install())
            self.driver = webdriver.Firefox

        elif self.browser.lower() == "edge":
            opt = EdgeOptions()
            serv = EdgeService(EdgeChromiumDriverManager().install())
            self.driver = webdriver.Edge

        elif self.browser.lower() == "safari":
            opt = SafariOptions()
            serv = None
            self.driver = webdriver.Safari

        return self.driver(service=serv, options=opt)
