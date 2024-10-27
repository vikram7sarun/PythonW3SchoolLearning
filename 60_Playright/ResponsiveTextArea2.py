import tkinter as tk
from tkinter import scrolledtext, END
from playwright.sync_api import sync_playwright


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
    selected_text = output_text.get("sel.first", "sel.last")
    moved_text.insert(END, selected_text + "\n")
    output_text.delete("sel.first", "sel.last")


# Function to generate POM based on moved selectors
def generate_pom():
    # Clear the moved_text area before generating the POM
    moved_text.delete(1.0, END)

    # Sample class name
    class_name = "SamplePage"

    # Collect selectors from the moved_text
    selectors = moved_text.get("1.0", END).strip().splitlines()

    # Start building the POM as a string
    pom_code = f"class {class_name}:\n    def __init__(self, page):\n        self.page = page\n\n"

    for idx, selector in enumerate(selectors):
        # Generating field name and method name based on selector type or line position
        field_name = f"element_{idx + 1}"

        # Add the selector as a class attribute and a method to interact with it
        pom_code += f"        self.{field_name} = '{selector}'\n"
        pom_code += f"\n    def click_{field_name}(self):\n        self.page.click(self.{field_name})\n"
        pom_code += f"\n    def get_{field_name}_text(self):\n        return self.page.text_content(self.{field_name})\n"

    # Insert the generated POM code into the moved_text area
    moved_text.insert(END, pom_code)


# Set up the tkinter UI
root = tk.Tk()
root.title("Selector Fetcher")

root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

# Create input label and entry box for selector priorities
label = tk.Label(root, text="Enter Selector Priorities (comma-separated):")
label.grid(row=0, column=0, sticky="w", padx=10, pady=(10, 2))

entry = tk.Entry(root, width=50)
entry.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 5))

fetch_button = tk.Button(root, text="Fetch Selectors", command=fetch_selectors)
fetch_button.grid(row=1, column=1, sticky="ew", padx=(0, 10), pady=(0, 5))

# Main text area to display the output selectors
output_text = scrolledtext.ScrolledText(root, width=60, height=10)
output_text.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=(5, 0))

# Button to move selected lines
move_button = tk.Button(root, text="Move Selected Lines", command=move_selected_lines)
move_button.grid(row=3, column=0, sticky="ew", padx=(10, 5), pady=5)

# Button to generate POM
generate_pom_button = tk.Button(root, text="Generate POM", command=generate_pom)
generate_pom_button.grid(row=3, column=1, sticky="ew", padx=(5, 10), pady=5)

# Second text area for moved selectors or generated POM
moved_text = scrolledtext.ScrolledText(root, width=60, height=10)
moved_text.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=10, pady=(0, 10))

root.mainloop()
