import os


# Function to generate a Page Object Model (POM) file for a given page
def generate_pom(page_name, elements):
    # Create a directory to store the POM files if it doesn't exist
    if not os.path.exists('pom_pages'):
        os.makedirs('pom_pages')

    # Define the filename for the POM
    filename = f'pom_pages/{page_name.lower()}_page.py'

    # Open the file for writing
    with open(filename, 'w') as file:
        # Write the imports for Selenium and other dependencies
        file.write('import logging\n')
        file.write('import time\n')
        file.write('import utilities.custom_logger as cl\n')
        file.write('from base.selenium_driver import Selenium_Driver\n\n')

        file.write(f'class {page_name.capitalize()}Page({"Selenium_Driver"}):\n\n')

        # Write main function
        file.write('    if __name__ == "__main__":\n')
        file.write('        log = cl.customLogger(logging.DEBUG)\n\n')


        # Write the constructor for the Page Object

        file.write('    """Page Object for {} page"""\n\n'.format(page_name.capitalize()))
        file.write('    def __init__(driver):\n')
        file.write('        super().__init__(driver)\n')
        file.write('        self.driver = driver\n\n')

        for element in elements:
            element_name = element['name']
            locator_type = element['type']
            locator_value = element['locator']
            file.write(f'       __{element_name} = "{locator_value}"\n')
            file.write('\n')

        # Write interaction methods for each element
        for element in elements:
            element_name = element['name']
            file.write(f'    def click_{element_name}(self):\n')
            file.write(f'        """Click the {element_name} element"""\n')
            file.write(f'        self.driver.find_element(*self.{element_name}_locator).click()\n\n')

            file.write(f'    def get_{element_name}_text(self):\n')
            file.write(f'        """Get the text of the {element_name} element"""\n')
            file.write(f'        return self.driver.find_element(*self.{element_name}_locator).text\n\n')

    print(f'Page Object Model (POM) for "{page_name}" has been generated successfully at "{filename}".')


# Example Usage of the Script
if __name__ == '__main__':
    # Example user input
    page_name = input("Enter the page name (e.g., Login, Home, etc.): ")

    # Example list of web elements to be included in the POM
    elements = [{'name': 'home_text', 'type': 'xpath', 'locator': "//*[text()='Home']"},
                {'name': 'password_text', 'type': 'xpath', 'locator': "//*[text()='Password:']"},
                {'name': 'log_in_text', 'type': 'xpath', 'locator': "//*[text()='Log In']"},
                {'name': 'email_text', 'type': 'xpath', 'locator': "//*[text()='Email:']"},
                {'name': 'to_continu_text', 'type': 'xpath', 'locator': "//*[contains(text(), 'To continu')]"},
                {'name': 'acme_syste_text', 'type': 'xpath', 'locator': "//*[contains(text(), 'ACME Syste')]"}]


    # Generate the POM code
    generate_pom(page_name, elements)
