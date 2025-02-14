import logging
import os
import pytest

from datetime import datetime

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
def init_driver_manager(dynamic_browser, test_logger):
    """
    Function yields driver instance
    Browser type is solved from dynamic_browser fixture
    """
    new_driver = DriverManager(dynamic_browser).get_driver()
    test_logger.info(f"Web driver created: {new_driver}")
    yield new_driver
    new_driver.quit()

# Ensure the directory for the current test run is created once per session
@pytest.fixture(scope='session', autouse=True)
def setup_session_logging(request):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    base_log_dir = os.path.join("logs", f"test_run_{now}")
    os.makedirs(base_log_dir, exist_ok=True)
    request.config.base_log_dir = base_log_dir


@pytest.fixture(scope='function', name="test_logger")
def test_logger(request):
    # Create a specific directory for each test within the test run directory
    test_name = request.node.name
    test_directory = os.path.join(request.config.base_log_dir, test_name)
    os.makedirs(test_directory, exist_ok=True)

    log_file_path = os.path.join(test_directory, "test.log")

    # Setup specific logger for the test
    logger = logging.getLogger(test_name)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file_path, mode='w')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
                                  '%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    yield logger

    # Do cleanup after the test is done
    file_handler.close()
    logger.removeHandler(file_handler)