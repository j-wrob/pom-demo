"""
Test suite for login page testing
"""
import pytest
from src.pages.loginpage import LoginPage

@pytest.mark.negative
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
    login_page.type_username("bad_username")
    login_page.type_password("bad_password")
    login_page.click_login()
    login_page.verify_invalid_login()

@pytest.mark.positive
def test_valid_login(driver):
    """
    Test to verify valid login scenario
    """
    login_page = LoginPage(driver=driver)

    login_page.get_url()
    login_page.type_username("tomsmith")
    login_page.type_password("SuperSecretPassword!")
    login_page.click_login()
    login_page.verify_valid_login()
