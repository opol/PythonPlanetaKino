import unittest as unittest
from selenium import webdriver
#from BasePage import LoginPage
from LoginPage import LoginPage


class loginTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://planetakino.ua/')

    def tearDown(self):
        self.driver.close()

    def test_LoginSuccess(self):
        login_page = LoginPage(self.driver)
        login_page.login('ulyana.opolska@gmail.com', 'banana')
        assert login_page.login_popup_displayed()
