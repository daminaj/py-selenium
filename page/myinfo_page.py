from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class MyInfoPage:
    def __init__(self, driver):
        self.driver = driver
        self.emp_first_name = (By.XPATH, "//input[@placeholder='First Name']")
        self.emp_last_name = (By.XPATH, "//input[@placeholder='Last Name']")
        self.emp_middle_name = (By.XPATH, "//input[@placeholder='Middle Name']")
        self.emp_license_date = (By.XPATH, "/(//input[@placeholder='yyyy-dd-mm'])[1]")
        self.save_btn = (By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[1]")



    def clear_field (self):
        actions = ActionChains(self.driver)
        actions.click()
        time.sleep(3)
        actions.key_down(Keys.CONTROL)
        actions.send_keys("a")
        actions.key_up(Keys.CONTROL)
        actions.send_keys(Keys.BACKSPACE)
        actions.perform()


    def edit_info (self, firstname, middlename, lastname):
        firstname_input = self.driver.find_element(*self.emp_first_name)
        # self.clear_field(firstname_input)
        firstname_input.clear()
        firstname_input.send_keys(firstname)

        middlename_input = self.driver.find_element(*self.emp_middle_name)
        # self.clear_field(middlename_input)
        middlename_input.clear()
        middlename_input.send_keys(middlename)

        lastname_input = self.driver.find_element(*self.emp_last_name)
        # self.clear_field(lastname_input)
        lastname_input.clear()
        lastname_input.send_keys(lastname)

        # licencedate_input = self.driver.find_element(*self.emp_license_date)
        # self.clear_field(licencedate_input)
        # licencedate_input.send_keys(licencedate)


    def click_save (self):
        self.driver.find_element(*self.save_btn).click()


   
       