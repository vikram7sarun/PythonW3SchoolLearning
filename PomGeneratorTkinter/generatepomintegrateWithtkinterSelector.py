import tkinter as tk
from tkinter import scrolledtext, END
from playwright.sync_api import sync_playwright
from tkinter import scrolledtext, END, filedialog
import re
import os


# Helper function to build a selector based on priority
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


# Main function to retrieve selectors and display them in the text area
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


# Function to move selected lines to the moved_text area
def move_selected_lines():
    try:
        # Capture selected text from output_text
        selected_text = output_text.get("sel.first", "sel.last")

        # Insert selected text into moved_text area
        moved_text.insert(END, selected_text + "\n")

        # Optionally, remove selected text from output_text if desired
        output_text.delete("sel.first", "sel.last")

    except tk.TclError:
        print("No text selected to move.")  # If no text is selected, an error will be caught here


# Placeholder management functions for the class name entry
def on_entry_click(event):
    """Remove placeholder text when the entry is focused."""
    if class_name_entry.get() == "Enter Class Name":
        class_name_entry.delete(0, "end")  # Clear the placeholder text
        class_name_entry.config(fg="black")  # Change text color to black

def on_focusout(event):
    """Restore placeholder text if the entry is empty."""
    if class_name_entry.get() == "":
        class_name_entry.insert(0, "Enter Class Name")  # Restore placeholder
        class_name_entry.config(fg="grey")  # Set placeholder text color


# Function to generate POM and display it in the moved_text area
def generate_pom():


    # Retrieve the class name from the class_name_entry box
    class_name = class_name_entry.get() or "TestPage"

    # Collect selectors from the moved_text and check content
    selectors = moved_text.get("1.0", END).strip().splitlines()

    # Debugging: Print the selectors list to verify it’s populated correctly
    # print("Captured selectors:", selectors)

    # Clear the moved_text area before generating the POM
    moved_text.delete(1.0, END)

    elements = []
    for selector in selectors:
        # Determine the name based on the type of selector
        if "@id='" in selector:
            # Extract ID value
            name_part = selector.split("@id='")[1].split("']")[0]
            name = f"{name_part}_id"
        elif "@name='" in selector:
            # Extract name attribute
            name_part = selector.split("@name='")[1].split("']")[0]
            name = f"{name_part}_name"
        elif "contains(@class," in selector:
            # Extract class values for combined class selectors
            classes = selector.split("contains(@class, '")
            class_names = "_".join(cls.split("')")[0] for cls in classes[1:])
            name = f"{class_names}_class"
        elif "text()=" in selector or "contains(text()," in selector:
            # Handle text-based selectors
            if "text()=" in selector:
                text_value = selector.split("text()='")[1].split("']")[0]
            else:
                text_value = selector.split("contains(text(), '")[1].split("')")[0]
            name = text_value.lower().replace(" ", "_").replace(":", "")
        else:
            name = "custom_selector"

        elements.append({
            'name': name,
            'type': 'xpath',
            'locator': selector
        })

    # Define the generated POM content
    pom_code = f"""import logging
import time
import utilities.custom_logger as cl
from base.selenium_driver import Selenium_Driver

class {class_name.capitalize()}Page(Selenium_Driver):

    log = cl.customLogger(logging.DEBUG)

    \"\"\"Page Object for {class_name}\"\"\"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
"""
    for element in elements:
        locator_name = f"__{element['name']}"
        pom_code += f"    {locator_name} = \"{element['locator']}\"\n"

    pom_code += "\n    # Functions\n"
    for element in elements:
        function_name = f"click_{element['name']}"
        pom_code += f"\n    def {function_name}(self):\n"
        pom_code += f"        self.elementClick(self.{locator_name}, locatorType='xpath')\n"

    # Display the generated POM in moved_text
    moved_text.insert(END, pom_code)

# Function to save the POM code in moved_text area to a .py file
def save_to_file():
    pom_code = moved_text.get("1.0", END)
    if pom_code.strip():  # Ensure there's content to save
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(pom_code)
            print(f"POM saved as {file_path}")



# Set up the tkinter UI
root = tk.Tk()
root.title("NessQ POM Creator")

# # Load and set the icon
# icon_path = "C:\\Vikram\\Codebase\\Python\\PythonW3SchoolLearning\\PomGeneratorTkinter\\Nessicon.png"   # Replace with your icon path
# root.iconphoto(False, tk.PhotoImage(file=icon_path))


# Colors
button_bg = "#dbe9f4"  # Light blue color for buttons
entry_bg = "#f7f9fc"   # Very light grey for entry and text areas
text_bg = "#e8eff5"    # Soft blue-grey for text areas

# Configure grid layout to make text areas responsive
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(4, weight=1)  # Make moved_text area also responsive

# Create input label and entry box for selector priorities
label = tk.Label(root, text="Enter Selector Priorities (comma-separated): \n ID, Name, ClassName, LinkText, "
                            "PartialLinkText, TagName", bg="#f0f4f8", fg="#333333")
label.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 2))

entry = tk.Entry(root, width=50, bg=entry_bg, fg="#333333", relief="solid")
entry.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 5))

fetch_button = tk.Button(root, text="Fetch Selectors", command=fetch_selectors, bg=button_bg, relief="groove")
fetch_button.grid(row=1, column=1, sticky="ew", padx=(0, 10), pady=(0, 5))

# Main text area to display the output selectors
output_text = scrolledtext.ScrolledText(root, width=60, height=10, bg=text_bg, fg="#333333", relief="solid")
output_text.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=10, pady=(5, 0))

# Button to move selected lines
move_button = tk.Button(root, text="Move Selected Lines", command=move_selected_lines, bg=button_bg, relief="groove")
move_button.grid(row=3, column=0, sticky="ew", padx=(10, 5), pady=5)

# Entry box for the class name
class_name_entry = tk.Entry(root, width=20, fg="grey", bg=entry_bg, relief="solid")
class_name_entry.insert(0, "Enter Class Name")  # Set placeholder text
class_name_entry.bind("<FocusIn>", on_entry_click)
class_name_entry.bind("<FocusOut>", on_focusout)
class_name_entry.grid(row=3, column=1, sticky="ew", padx=(5, 10), pady=5)

# Button to generate POM
generate_pom_button = tk.Button(root, text="Generate POM", command=generate_pom, bg=button_bg, relief="groove")
generate_pom_button.grid(row=3, column=2, sticky="ew", padx=(5, 10), pady=5)

# Second text area for moved selectors or generated POM
moved_text = scrolledtext.ScrolledText(root, width=70, height=10, bg=text_bg, fg="#333333", relief="solid")
moved_text.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=10, pady=(0, 10))

# Button to download code
download_button = tk.Button(root, text="Download Code", command=save_to_file, bg=button_bg, relief="groove")
download_button.grid(row=3, column=3, sticky="ew", padx=(5, 10), pady=5)


root.mainloop()
