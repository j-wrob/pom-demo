"""
Test suite for dropdown page testing
"""
import pytest
from src.pages.dropdownpage import DropdownPage


def test_loading_page(driver, test_logger):
    """
    test docstring
    """
    test_logger.info(f"Log message from the test.")
    dropdown_page = DropdownPage(driver, test_logger)
    dropdown_page.get_url()

@pytest.mark.parametrize(
    "value", ["1","2"]
)
def test_selecting_elements(driver, value, test_logger):
    """
    test docstring
    """
    test_logger.info(f"Log message from the test.")
    dropdown_page = DropdownPage(driver, test_logger)
    dropdown_page.get_url()
    dropdown_page.select_from_dropdown_by_value(value)
