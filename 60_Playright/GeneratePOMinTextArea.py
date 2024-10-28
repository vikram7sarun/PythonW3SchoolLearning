import os
import tkinter as tk
from tkinter import scrolledtext, END
import re

from playwright.async_api import PlaywrightContextManager


# Define the generate_pom function as specified
def generate_pom(page_name, elements):
    pom_code = ""

    # Write the imports for Selenium and other dependencies
    pom_code += 'import logging\n'
    pom_code += 'import time\n'
    pom_code += 'import utilities.custom_logger as cl\n'
    pom_code += 'from base.selenium_driver import Selenium_Driver\n\n'

    pom_code += f'class {page_name.capitalize()}Page(Selenium_Driver):\n\n'

    # Write main function
    pom_code += '    if __name__ == "__main__":\n'
    pom_code += '        log = cl.customLogger(logging.DEBUG)\n\n'

    # Write the constructor for the Page Object
    pom_code += f'    """Page Object for {page_name.capitalize()} page"""\n\n'
    pom_code += '    def __init__(self, driver):\n'
    pom_code += '        super().__init__(driver)\n'
    pom_code += '        self.driver = driver\n\n\n'

    pom_code += '    """locators"""\n\n'
    for element in elements:
        element_name = element['name']
        locator_type = element['type']
        locator_value = element['locator'].replace('"', "'")
        pom_code += f'    __{element_name} = "{locator_value}"\n'
    pom_code += '\n\n'

    pom_code += '    """Functions"""\n\n'
    for element in elements:
        element_name = element['name']
        pom_code += f'    def click_{element_name}(self):\n'
        pom_code += f'        """Click the {element_name} element"""\n'
        pom_code += f'        self.driver.find_element(*self.__{element_name}).click()\n\n'
    pom_code += '\n\n'

    return pom_code

def get_priority_selector(element):
    try:
        element_id = element.evaluate("element => element.id")
        if element_id:
            return f"//*[@id='{element_id}']"

        name_attr = element.evaluate("element => element.getAttribute('name')")
        if name_attr:
            return f"//*[@name='{name_attr}']"

        class_attr = element.evaluate("element => element.className")
        if class_attr:
            class_name = " and ".join([f"contains(@class, '{cls}')" for cls in class_attr.split()])
            return f"//*[{class_name}]"

        inner_text = element.evaluate("element => element.innerText").strip() if element.evaluate(
            "element => element.innerText") else ""
        if inner_text and len(inner_text) <= 10:
            return f"//*[text()='{inner_text}']"

        if inner_text and len(inner_text) > 10:
            return f"//*[contains(text(), '{inner_text[:10]}')]"

        tag_name = element.evaluate("element => element.tagName.toLowerCase()")
        if tag_name:
            return f"//{tag_name}"

    except Exception as e:
        print(f"Error generating selector for element: {e}")

    return None


def fetch_selectors():
    desired_priorities = entry.get().split(",")
    desired_priorities = [priority.strip() for priority in desired_priorities]

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9214")
        default_context = browser.contexts[0]
        page = default_context.pages[0]
        page.wait_for_load_state("load")

        selectors_by_priority = {
            "ID": set(),
            "Name": set(),
            "ClassName": set(),
            "LinkText": set(),
            "PartialLinkText": set(),
            "TagName": set(),
        }

        elements = page.query_selector_all("*")
        for element in elements:
            try:
                selector = get_priority_selector(element)

                if selector:
                    if "id=" in selector:
                        selectors_by_priority["ID"].add(selector)
                    elif "name=" in selector:
                        selectors_by_priority["Name"].add(selector)
                    elif "contains(@class," in selector:
                        selectors_by_priority["ClassName"].add(selector)
                    elif "text()=" in selector:
                        selectors_by_priority["LinkText"].add(selector)
                    elif "contains(text()," in selector:
                        selectors_by_priority["PartialLinkText"].add(selector)
                    elif selector.startswith("//"):
                        selectors_by_priority["TagName"].add(selector)

            except Exception as e:
                print(f"Error processing element: {e}")

        output_text.delete(1.0, END)  # Clear previous output
        for priority in desired_priorities:
            if priority in selectors_by_priority:
                output_text.insert(END, f"\n{priority} Selectors:\n")
                for selector in selectors_by_priority[priority]:
                    output_text.insert(END, f"{selector}\n")
            else:
                output_text.insert(END, f"\nNo selectors found for priority: {priority}\n")

        browser.close()
def sync_playwright() -> PlaywrightContextManager:
    return PlaywrightContextManager()

# Function to move selected lines to the moved_text area
def move_selected_lines():
    selected_text = output_text.get("sel.first", "sel.last")
    moved_text.insert(END, selected_text + "\n")
    output_text.delete("sel.first", "sel.last")


# Function to parse the contents of moved_text and generate the POM
def generate_pom_in_text_area():
    moved_text.delete(1.0, END)  # Clear the moved_text area before generating the POM

    # Retrieve the class name from the class_name_entry box
    page_name = class_name_entry.get() or "TestPage"  # Default to "TestPage" if the entry is empty

    # Collect selectors from the moved_text
    selectors = moved_text.get("1.0", END).strip().splitlines()

    # Prepare the elements list required for the POM function
    elements = []
    for selector in selectors:
        match = re.search(r"text\(\)='([^']+)'", selector)
        if match:
            # Generate element details
            element_name = match.group(1).replace(" ", "_").replace(":", "").lower()
            element = {'name': element_name, 'type': 'xpath', 'locator': selector}
            elements.append(element)
        else:
            # Display unmatched selector in the output to troubleshoot
            moved_text.insert(END, f"# Unmatched selector format: {selector}\n")

    # Call the generate_pom function and get the POM code
    pom_code = generate_pom(page_name, elements)

    # Display the generated POM code in moved_text area
    moved_text.insert(END, pom_code)


# Set up the tkinter UI
root = tk.Tk()
root.title("Selector Fetcher")

# Configure grid layout to make text areas responsive
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(4, weight=1)  # Make moved_text area also responsive

# Create input label and entry box for selector priorities
label = tk.Label(root, text="Enter Selector Priorities (comma-separated):")
label.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 2))

entry = tk.Entry(root, width=50)
entry.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 5))

fetch_button = tk.Button(root, text="Fetch Selectors", command=fetch_selectors)
fetch_button.grid(row=1, column=1, sticky="ew", padx=(0, 10), pady=(0, 5))

# Main text area to display the output selectors
output_text = scrolledtext.ScrolledText(root, width=60, height=10)
output_text.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=10, pady=(5, 0))

# Button to move selected lines
move_button = tk.Button(root, text="Move Selected Lines", command=move_selected_lines)
move_button.grid(row=3, column=0, sticky="ew", padx=(10, 5), pady=5)

# Entry box for the class name
class_name_entry = tk.Entry(root, width=20)
class_name_entry.grid(row=3, column=1, sticky="ew", padx=(5, 10), pady=5)

# Button to generate POM
generate_pom_button = tk.Button(root, text="Generate POM", command=generate_pom_in_text_area)
generate_pom_button.grid(row=3, column=2, sticky="ew", padx=(5, 10), pady=5)

# Second text area for moved selectors or generated POM
moved_text = scrolledtext.ScrolledText(root, width=60, height=10)
moved_text.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=10, pady=(0, 10))

root.mainloop()
