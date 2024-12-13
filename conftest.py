import pytest
import os

from selenium import webdriver
from selenium.webdriver import ChromeService
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import FirefoxOptions
from selenium.webdriver import FirefoxService


def pytest_addoption(parser):
    """
    Function to use in order to define browser in pytest command
    It is a precondition for request.config.getoption("--browser")
    """
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="chrome, edge, firefox, safari"
    )

# METHOD 1
# @pytest.fixture(name="driver", scope="module", name="driver")
# def driver_init(request):
#     """
#     Init driver according to pytest command arg --browser
#     """
#     browser = request.config.getoption("--browser")
#     if browser == 'chrome':
#
#         #default would be chrome
#         options = ChromeOptions()
#         service = ChromeService(ChromeDriverManager().install())
#         webdriver_class = webdriver.Chrome
#
#     if browser == 'firefox':
#         install_dir = "/snap/firefox/current/usr/lib/firefox"
#         driver_loc = os.path.join(install_dir, "geckodriver")
#         binary_loc = os.path.join(install_dir, "firefox")
#         service = FirefoxService(driver_loc)
#
#         options = FirefoxOptions()
#         options.binary_location = binary_loc
#         webdriver_class = webdriver.Firefox
#
#     with webdriver_class(service=service, options=options) as driver:
#         yield driver
#         driver.quit()

# METHOD 2
@pytest.fixture(params=["chrome", "firefox"], scope="module", name="driver")
def driver_init(request):
    """
    Parametrize browsers in fixture
    """
    browser = request.param

    if browser == 'chrome':
        options = ChromeOptions()
        service = ChromeService(ChromeDriverManager().install())
        webdriver_class = webdriver.Chrome

    if browser == 'firefox':
        install_dir = "/snap/firefox/current/usr/lib/firefox"
        driver_loc = os.path.join(install_dir, "geckodriver")
        binary_loc = os.path.join(install_dir, "firefox")
        service = FirefoxService(driver_loc)

        options = FirefoxOptions()
        options.binary_location = binary_loc
        webdriver_class = webdriver.Firefox

    with webdriver_class(service=service, options=options) as driver:
        yield driver
    driver.quit()