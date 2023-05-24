# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, "//input[@value='Log In']")
    
    def enter_username(self, username):
        self.driver.find_element(*self.username_field).clear()
        self.driver.find_element(*self.username_field).send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)
    
    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.right_panel_heading = (By.XPATH, "//div[@id='rightPanel']/div/div/h1")
        self.left_panel_heading = (By.XPATH, "//div[@id='leftPanel']/h2")
        self.account_table_header = (By.XPATH, "//table[@id='accountTable']/thead/tr/th")
    
    def click_right_panel_heading(self):
        self.driver.find_element(*self.right_panel_heading).click()
    
    def click_left_panel_heading(self):
        self.driver.find_element(*self.left_panel_heading).click()
    
    def get_account_table_header(self):
        return self.driver.find_element(*self.account_table_header)

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        yield
        self.driver.quit()
        assert self.verificationErrors == []

    def test_login(self):
        driver = self.driver
        driver.get("https://parabank.parasoft.com/parabank/")
        
        login_page = LoginPage(driver)
        login_page.enter_username("TestUser_RafaelOliveira")
        login_page.enter_password("Pc!Dau2LeLu4L")
        login_page.click_login_button()
        
        account_page = AccountPage(driver)
        account_page.click_right_panel_heading()
        account_page.click_left_panel_heading()
        account_table_header = account_page.get_account_table_header()
        
        assert account_table_header is not None
    
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True
    
    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException:
            return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True