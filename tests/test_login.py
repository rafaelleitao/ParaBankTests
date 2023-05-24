import pytest
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.helpers import is_element_present, is_alert_present, close_alert_and_get_its_text

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=r'path/to/chromedriver')
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

        assert is_element_present(driver, By.XPATH, "//table[@id='accountTable']/thead/tr/th")
        #assert is_alert_present(driver)
        #alert_text = close_alert_and_get_its_text(driver)
        #assert alert_text == "Expected alert text"