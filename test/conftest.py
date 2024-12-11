import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 

@pytest.fixture(scope="session")
def driver():
    """Initialize and clean up the WebDriver."""
    service = Service(ChromeDriverManager().install())
    option=Options()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=option)
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    # driver.quit()