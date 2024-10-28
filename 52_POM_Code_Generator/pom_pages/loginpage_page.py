from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """Page Object for Loginpage page"""

    def __init__(self, driver):
        self.driver = driver

        self.username_field_locator = (By.ID, "username")
        self.password_field_locator = (By.ID, "password")
        self.login_button_locator = (By.XPATH, "//button[@type='submit'']")

    def get_username_field_text(self):
        """Get the text of the username_field element"""
        return self.driver.find_element(*self.username_field_locator).text

    def click_password_field(self):
        """Click the password_field element"""
        self.driver.find_element(*self.password_field_locator).click()

    def click_login_button(self):
        """Click the login_button element"""
        self.driver.find_element(*self.login_button_locator).click()

    def get_login_button_text(self):
        """Get the text of the login_button element"""
        return self.driver.find_element(*self.login_button_locator).text

