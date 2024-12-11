from selenium.webdriver.common.by import By
import time


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.my_info = (By.XPATH, "//span[normalize-space()='My Info']")
        self.avater = (By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
        self.logout = (By.XPATH, "//a[normalize-space()='Logout']")


    def click_my_info(self):
        self.driver.find_element(*self.my_info).click()

    def click_logout(self):
        self.driver.find_element(*self.avater).click()
        time.sleep(5)
        self.driver.find_element(*self.logout).click()