"""
Test suite for login page testing
"""
import pytest
from src.pages.login_page import LoginPage

@pytest.mark.usefixtures()
@pytest.mark.parametrize(
    "username, password", [
        ("wrongusername", "wrongpassword"),
        ("wrongusername", "SuperSecretPassword!"),
        ("", "SuperSecretPassword!"),
        ("tomsmith", "wrongpassword"),
        ("tomsmith", "")
    ]
)
def test_invalid_login(driver, username, password):
    """
    Tests to verify invalid login scenarios
    """
    login_page = LoginPage(driver=driver)

    login_page.get_url()
    login_page.select_username("bad_username")
    login_page.select_password("bad_password")
    login_page.click_login()
    login_page.verify_invalid_login()


def test_valid_login(driver):
    """
    Test to verify valid login scenario
    """
    login_page = LoginPage(driver=driver)

    login_page.get_url()
    login_page.select_username("tomsmith")
    login_page.select_password("SuperSecretPassword!")
    login_page.click_login()
    login_page.verify_valid_login()

def test_just_to_be_skipped(driver):
    """
    Could be Safari only test
    """
    if driver.capabilities["browserName"] in ['chrome', 'firefox']:
        pytest.skip("Features not supported by Chrome and Firefox")