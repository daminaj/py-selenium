from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# from pynput.keyboard import Key, Controller
import time


service = Service(ChromeDriverManager().install())
option=Options()
option.add_experimental_option("detach", True)
drive = webdriver.Chrome(service=service, options=option)
drive.maximize_window()
drive.implicitly_wait(20)
drive.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# login
username=drive.find_element(By.XPATH, "//input[@placeholder='Username']")
username.send_keys("Admin")
password=drive.find_element(By.XPATH, "//input[@placeholder='Password']")
password.send_keys("admin123")
loginBtn=drive.find_element(By.XPATH, "//button[normalize-space()='Login']")
loginBtn.click()


######### Home Page Actions ######
usrProfile = drive.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
usrProfile.click()

about = drive.find_element(By.XPATH, "//a[normalize-space()='About']")
about.click()

closeAboutModal = drive.find_element(By.XPATH, "//button[normalize-space()='×']")
closeAboutModal.click()

usrProfile = drive.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
usrProfile.click()
time.sleep(5)

support = drive.find_element(By.XPATH, "//a[normalize-space()='Support']")
support.click()

time.sleep(5)

drive.back()



########## My Info Page Actions ##################
myInfoMenu = drive.find_element(By.XPATH, "//span[normalize-space()='My Info']")
myInfoMenu.click()

drive.refresh()
firstName = drive.find_element(By.XPATH, "//input[@placeholder='First Name']")
actions = ActionChains(drive)
actions.click(firstName)
time.sleep(3)
actions.key_down(Keys.CONTROL)
actions.send_keys("a")
actions.key_up(Keys.CONTROL)
actions.send_keys(Keys.BACKSPACE)
actions.perform()
firstName.send_keys("Agbabiaka")

middleName = drive.find_element(By.XPATH, "//input[@placeholder='Middle Name']")
actions.click(middleName)
time.sleep(3)
actions.key_down(Keys.CONTROL)
actions.send_keys("a")
actions.key_up(Keys.CONTROL)
actions.send_keys(Keys.BACKSPACE)
actions.perform()
middleName.send_keys("AgbAyinde")

lastName = drive.find_element(By.XPATH, "//input[@placeholder='Last Name']")
actions.click(lastName)
time.sleep(3)
actions.key_down(Keys.CONTROL)
actions.send_keys("a")
actions.key_up(Keys.CONTROL)
actions.send_keys(Keys.BACKSPACE)
actions.perform()
lastName.send_keys("Ekom")

# employeeID = drive.find_element(By.CLASS_NAME, "oxd-input oxd-input--active")
# actions.click(employeeID)
# time.sleep(3)
# actions.key_down(Keys.CONTROL)
# actions.send_keys("a")
# actions.key_up(Keys.CONTROL)
# actions.send_keys(Keys.BACKSPACE)
# actions.perform()
# employeeID.send_keys("23eed2")

driverLicence = drive.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[4]")
actions.click(driverLicence)
time.sleep(3)
actions.key_down(Keys.CONTROL)
actions.send_keys("a")
actions.key_up(Keys.CONTROL)
actions.send_keys(Keys.BACKSPACE)
actions.perform()
driverLicence.send_keys("xhyt23386648")


# licenceDate = drive.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]")
# actions.click(licenceDate)
# time.sleep(3)
# actions.key_down(Keys.CONTROL)
# actions.send_keys("a")
# actions.key_up(Keys.CONTROL)
# actions.send_keys(Keys.BACKSPACE)
# actions.perform()
# licenceDate.send_keys("2026-10-09")

#######################3 DROP DOWN ################################


nationalityDropdown = WebDriverWait(drive, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='oxd-select-text oxd-select-text--active'][1]"))
)
nationalityDropdown.click()

dropdownOption = WebDriverWait(drive, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//span[text()='Algerian']"))  # Example option 'Indian'
)
dropdownOption.click()


########## UPLOAD FILE  #######

# addFile = drive.find_element(By.XPATH, "//button[normalize-space()='Add']")
# addFile.click()

# uploadFile = drive.find_element(By.XPATH, "(//div[@class='oxd-file-div oxd-file-div--active'])[1]")
# uploadFile.click()
# keyboard = Controller
# keyboard.type('/home/shams/Downloads/cat.jpg/')
# keyboard.press(Key.enter)
# keyboard.release(Key.enter)

# uploadFile.send_keys("/home/shams/Downloads/cat.jpg")
# saveupld = drive.find_element(By.XPATH, "//div[@class='orangehrm-attachment']//button[@type='submit'][normalize-space()='Save']")
# saveupld.click()


####### save edits
savebtn = drive.find_element(By.CSS_SELECTOR, "div[class='orangehrm-horizontal-padding orangehrm-vertical-padding'] button[type='submit']")
savebtn.click()
time.sleep(2)


############### PIM Page Actions ################
pim = drive.find_element(By.XPATH, "//span[normalize-space()='PIM']")
pim.click()

addPim = drive.find_element(By.XPATH, "//button[normalize-space()='Add']")
addPim.click()


empFirstName = drive.find_element(By.XPATH, "//input[@placeholder='First Name']")
empFirstName.send_keys("Ojo")

empMiddleName = drive.find_element(By.XPATH, "//input[@placeholder='Middle Name']")
empMiddleName.send_keys("Bidemi")

empLastName = drive.find_element(By.XPATH, "//input[@placeholder='Last Name']")
empLastName.send_keys("Alakija")

empID = drive.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
actions.click(empID)
time.sleep(3)
actions.key_down(Keys.CONTROL)
actions.send_keys("a")
actions.key_up(Keys.CONTROL)
actions.send_keys(Keys.BACKSPACE)
actions.perform()
empID.send_keys("emp23445")

createLogin = drive.find_element(By.XPATH, "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]")
createLogin.click()

#####Login details######

empUsername = drive.find_element(By.XPATH, "(//input[@autocomplete='off'])[1]")
empUsername.send_keys("Abudu")

empPass = drive.find_element(By.XPATH, "(//input[@type='password'])[1]")
empPass.send_keys("SaliuSule1")

empPass = drive.find_element(By.XPATH, "(//input[@type='password'])[2]")
empPass.send_keys("SaliuSule1")


drive.find_element(By.XPATH, "//button[normalize-space()='Save']").click()


drive.switch_to.new_window('tab')
WebDriverWait(drive, 10).until(EC.number_of_windows_to_be(2))
drive.switch_to.window(drive.window_handles[-1])

drive.get("https://www.saucedemo.com/")

