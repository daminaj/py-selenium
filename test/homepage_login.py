import pytest
from page.home_page import HomePage

@pytest.mark.dependency(name="test_valid_login")
def test_homepage_navigation(driver):
    """Test navigation to My Info page from the homepage."""
    # Initialize the HomePage object
    home_page = HomePage(driver)

    # Navigate to "My Info"
    home_page.click_my_info()


@pytest.mark.dependency(depends=["test_valid_login"])
def test_logout(driver):
    """Test logout functionality."""
    # Initialize the HomePage object
    home_page = HomePage(driver)

    # Perform logout
    home_page.click_logout()

 