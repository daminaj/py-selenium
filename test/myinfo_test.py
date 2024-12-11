import pytest
from page.myinfo_page import MyInfoPage
import time

@pytest.mark.dependency(depends=["test_valid_login"])
def test_edit_my_info(driver):
    """Test editing and saving personal information on My Info page."""
    # Initialize the MyInfoPage object
    my_info_page = MyInfoPage(driver)

    # Edit and save personal information
    # my_info_page.clear_field()
    my_info_page.edit_info("abioal", "Ajayi", "Ibrahim")
    time.sleep(5)
    my_info_page.click_save()

    driver.back()
