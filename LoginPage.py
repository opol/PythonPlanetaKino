import self as self
from selenium.webdriver.common.by import By


# This is the base page which defines attributes and methods that all other pages will share

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.timeout = 30


# This class represents the login page which defines attributes and methods associated with the login page

class LoginPage(BasePage):
    entranceBtn = (By.XPATH, './/*[@id=\'auth_block\']/div[1]/a[1]')
    email = (By.ID, 'txtEmail')
    password = (By.ID, 'password')
    submitButton = (By.XPATH, './/*[@id=\'enter_forma\']/div[3]/input')
    loginPopup = (By.XPATH, './/*[@id=\'activation-form\']/div')

    def set_email(self, email):
        emailElement = self.driver.find_element(*LoginPage.email)
        emailElement.clear()
        emailElement.send_keys(email)

    def set_password(self, password):
        pwordElement = self.driver.find_element(*LoginPage.password)
        pwordElement.send_keys(password)

    def login_popup_displayed(self):
        notifcationElement = self.driver.find_element(*LoginPage.loginPopup)
        return notifcationElement.is_displayed()

    def click_submit(self):
        submitBttn = self.driver.find_element(*LoginPage.submitButton)
        submitBttn.click()

    def click_entranceBtn(self):
        entranceButton = self.driver.find_element(*LoginPage.entranceBtn)
        entranceButton.click()


    def login(self, email, password):
        self.click_entranceBtn()
        self.set_password(password)
        self.set_email(email)
        self.click_submit()
