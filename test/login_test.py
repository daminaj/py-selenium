
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from page.login_page import LoginPage
from page.home_page import HomePage
from page.myinfo_page import MyInfoPage
import sys
import os
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    option=Options()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=option)
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    time.sleep(10)
    # driver.quit()
    
def test_valid_login(driver):
   
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")


    homepage = HomePage(driver)
    homepage.click_my_info()


    my_info_page = MyInfoPage(driver)
    # my_info_page.clear_field()
    my_info_page.edit_info("abioal", "Ajayi", "Ibrahim")
    time.sleep(5)
    my_info_page.click_save()

    driver.back()

    homepage.click_logout()

    
    


