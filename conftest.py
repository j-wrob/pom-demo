import pytest
from src.driver_manager.driver_manager import DriverManager


def pytest_configure(config):
    config.addinivalue_line("markers", "negative: mark test as a negative scenario test")
    config.addinivalue_line("markers", "positive: mark test as a positive scenario test")
    config.my_global_variable = "Shared data from pytest config"

def pytest_addoption(parser):
    """
    Function to use in order to define browser in pytest command
    It is a precondition for request.config.getoption("--browser")
    """
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="use browser dynamically: all /chrome / edge / firefox / safari"
    )

def pytest_generate_tests(metafunc):
    """
    Metafunc - metadata object used to modify the parameters of a test function.
    In this case fixture dynamic_browser appears in metafunc.fixturenames
    Because it's requested by init_driver_manager, but it's not defined anywhere.
    Since it's not defined the metafunc creates parameter dynamic_browser with various values
    """

    if "dynamic_browser" in metafunc.fixturenames:
        browser_value = metafunc.config.getoption("browser")

        if browser_value is None:
            raise Exception("Browser not specified! Use --browser flag.")
        elif browser_value == "all":
            # All available browsers
            params = ["chrome", "firefox", "edge", "safari"]
            metafunc.parametrize("dynamic_browser", params, scope="function")
        elif browser_value in ["chrome", "firefox", "edge", "safari"]:
            # If browser is specified, just provide it directly
            params = [browser_value]
            metafunc.parametrize("dynamic_browser", params, scope="function")
        else:
            # No browser - no tests
            raise Exception("Browser from outside of chrome/firefox/edge/safari")


@pytest.fixture(name="driver")
def init_driver_manager(get_x_value,
                        dynamic_browser):
    """
    Function yields driver instance
    Browser type is solved from dynamic_browser fixture
    """
    new_driver = DriverManager(dynamic_browser).get_driver()
    yield new_driver
    new_driver.quit()