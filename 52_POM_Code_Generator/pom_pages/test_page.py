import logging
import time
import utilities.custom_logger as cl
from base.selenium_driver import Selenium_Driver

class TestPage(Selenium_Driver):

    if __name__ == "__main__":
        log = cl.customLogger(logging.DEBUG)

    """Page Object for Test page"""

    def __init__(driver):
        super().__init__(driver)
        self.driver = driver

       __home_text = "//*[text()='Home']"

       __password_text = "//*[text()='Password:']"

       __log_in_text = "//*[text()='Log In']"

       __email_text = "//*[text()='Email:']"

       __to_continu_text = "//*[contains(text(), 'To continu')]"

       __acme_syste_text = "//*[contains(text(), 'ACME Syste')]"

    def click_home_text(self):
        """Click the home_text element"""
        self.driver.find_element(*self.home_text_locator).click()

    def get_home_text_text(self):
        """Get the text of the home_text element"""
        return self.driver.find_element(*self.home_text_locator).text

    def click_password_text(self):
        """Click the password_text element"""
        self.driver.find_element(*self.password_text_locator).click()

    def get_password_text_text(self):
        """Get the text of the password_text element"""
        return self.driver.find_element(*self.password_text_locator).text

    def click_log_in_text(self):
        """Click the log_in_text element"""
        self.driver.find_element(*self.log_in_text_locator).click()

    def get_log_in_text_text(self):
        """Get the text of the log_in_text element"""
        return self.driver.find_element(*self.log_in_text_locator).text

    def click_email_text(self):
        """Click the email_text element"""
        self.driver.find_element(*self.email_text_locator).click()

    def get_email_text_text(self):
        """Get the text of the email_text element"""
        return self.driver.find_element(*self.email_text_locator).text

    def click_to_continu_text(self):
        """Click the to_continu_text element"""
        self.driver.find_element(*self.to_continu_text_locator).click()

    def get_to_continu_text_text(self):
        """Get the text of the to_continu_text element"""
        return self.driver.find_element(*self.to_continu_text_locator).text

    def click_acme_syste_text(self):
        """Click the acme_syste_text element"""
        self.driver.find_element(*self.acme_syste_text_locator).click()

    def get_acme_syste_text_text(self):
        """Get the text of the acme_syste_text element"""
        return self.driver.find_element(*self.acme_syste_text_locator).text

