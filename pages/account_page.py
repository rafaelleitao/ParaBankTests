from selenium.webdriver.common.by import By

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