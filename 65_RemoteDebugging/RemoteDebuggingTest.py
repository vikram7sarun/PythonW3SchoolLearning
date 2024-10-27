import logging
import time
# import utilities.custom_logger as cl
# from base.selenium_driver import Selenium_Driver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pyautogui
import clipboard


class PageObjectExtractor():
    if __name__ == "__main__":
        pass
        # log = cl.customLogger(logging.DEBUG)

    """Page Object for dynamically extracted selectors"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def extract_selector(self, element):
        """Extracts selector from a given web element."""
        # Here we are assuming you will be using CSS selector for simplicity
        selector = element.get_attribute('outerHTML')
        return selector

    def get_page_selectors(self):
        """Interact with the browser to get elements and create POM."""
        # Assume you want to extract specific elements, e.g., inputs and buttons
        elements = self.driver.find_elements(By.XPATH, "//input | //button | //a")
        selectors = {}

        for element in elements:
            tag_name = element.tag_name
            selector = self.extract_selector(element)

            # Generate a unique key for each selector
            key = f"{tag_name}_{len(selectors) + 1}"
            selectors[key] = selector

        return selectors

    def create_pom(self, selectors):
        """Creates a POM based on the extracted selectors."""
        pom_script = """import logging\nimport utilities.custom_logger as cl\nfrom base.selenium_driver import Selenium_Driver\n\nclass ExtractedPage(Selenium_Driver):\n    if __name__ == "__main__":\n        log = cl.customLogger(logging.DEBUG)\n\n    def __init__(self, driver):\n        super().__init__(driver)\n        self.driver = driver\n\n"""

        # Define locators
        pom_script += "    \"\"\"Locators\"\"\"\n"
        for key, selector in selectors.items():
            # Example: Use CSS selector or XPath for locators
            pom_script += f"    __{key} = \"{selector}\"\n"

        # Define functions to interact with elements
        pom_script += "\n    \"\"\"Functions\"\"\"\n"
        for key in selectors.keys():
            pom_script += f"    def click_{key}(self):\n        \"\"\"Click {key} element\"\"\"\n        self.driver.find_element_by_css_selector(self.__{key}).click()\n\n"

        # Save the generated POM script to a file
        with open('extracted_page_object.py', 'w') as f:
            f.write(pom_script)


if __name__ == "__main__":
    # Initialize the Chrome WebDriver
    chrome_options = Options()
    # chrome_options.add_experimental_option("debuggerAddress", "http://localhost:9214")
    chrome_options.add_argument('--remote-debugging-port=9214')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://acme-test.uipath.com/")
    driver.find_element(By.ID, 'email').send_keys("vikic3110@gmail.com")
    driver.find_element(By.ID, 'password').send_keys("Test@123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # # Make sure the browser window is already opened to the desired URL
    # input("Press Enter after navigating to the desired webpage...")

    page_extractor = PageObjectExtractor(driver)
    extracted_selectors = page_extractor.get_page_selectors()
    page_extractor.create_pom(extracted_selectors)

    print("Page Object Model has been created and saved as 'extracted_page_object.py'.")
    driver.quit()