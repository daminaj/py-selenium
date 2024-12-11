from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 



class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.usern_input = (By.XPATH, "//input[@placeholder='Username']")
        self.pword_input = (By.XPATH, "//input[@placeholder='Password']")
        self.logbtn = (By.XPATH, "//button[normalize-space()='Login']")

    def nta_username(self, usernma):
        self.driver.find_element(*self.usern_input).send_keys(usernma)

    def nta_password(self, pword):
        self.driver.find_element(*self.pword_input).send_keys(pword)


    def click_login_btn(self):
        self.driver.find_element(*self.logbtn).click()

    def login(self, usernma, pword):
        self.nta_username(usernma)
        self.nta_password(pword)
        self.click_login_btn()  



        
