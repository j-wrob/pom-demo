"""
Test suite for home page testing
"""
import pytest
from src.pages.homepage import HomePage


def test_loading_page(driver):
    home_page = HomePage(driver)
    home_page.get_url()

def test_to_generate_fail():
    assert 1 == 0

def test_just_to_be_skipped(driver, request):
    """
    Could be Safari only test
    """
    my_var = request.config.my_global_variable
    print(f"My shared global variable from pytest_config: {my_var}")

    if driver.capabilities["browserName"] in ['chrome', 'firefox']:
        pytest.skip("Features not supported by Chrome and Firefox")