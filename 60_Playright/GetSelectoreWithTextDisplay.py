from playwright.sync_api import sync_playwright


# Helper function to build XPath for an element
def get_xpath(element):
    try:
        # Check for ID
        element_id = element.evaluate("element => element.id")
        if element_id:
            return f"//*[@id='{element_id}']"

        # Check for Name attribute
        name_attr = element.evaluate("element => element.getAttribute('name')")
        if name_attr:
            return f"//*[@name='{name_attr}']"

        # Check for ClassName
        class_attr = element.evaluate("element => element.className")
        if class_attr:
            # Generate XPath for ClassName (assumes all classes need to be matched)
            class_name = " and ".join([f"contains(@class, '{cls}')" for cls in class_attr.split()])
            return f"//*[{class_name}]"

        # Check for LinkText (exact match)
        inner_text = element.evaluate("element => element.innerText").strip()
        if inner_text and len(inner_text) <= 10:
            return f"//*[text()='{inner_text}']"

        # Check for Partial LinkText (partial match)
        if inner_text and len(inner_text) > 10:
            return f"//*[contains(text(), '{inner_text[:10]}')]"

        # Use TagName if nothing else matches
        tag_name = element.evaluate("element => element.tagName.toLowerCase()")
        if tag_name:
            return f"//{tag_name}"

        # Fallback to a basic CSS selector if no other match was found
        css_selector = element.evaluate("element => element.getAttribute('css')")
        if css_selector:
            return f"//{tag_name}[contains(@style, '{css_selector}')]"

    except Exception as e:
        print(f"Error generating XPath for element: {e}")

    return None  # If no matching attribute found for XPath


# Function to find a specific type of selector
def get_specific_selector(element, selector_type):
    try:
        # Check each selector type based on user input
        if selector_type.lower() == "id":
            element_id = element.evaluate("element => element.id")
            return f"id={element_id}" if element_id else None

        elif selector_type.lower() == "name":
            name_attr = element.evaluate("element => element.getAttribute('name')")
            return f"name={name_attr}" if name_attr else None

        elif selector_type.lower() == "classname":
            class_attr = element.evaluate("element => element.className")
            if class_attr:
                class_name = ".".join(class_attr.split())
                return f"class={class_name}"
            return None

        elif selector_type.lower() == "linktext":
            inner_text = element.evaluate("element => element.innerText").strip()
            if inner_text and len(inner_text) <= 10:  # Exact text
                return f"text={inner_text}"
            return None

        elif selector_type.lower() == "partial linktext":
            inner_text = element.evaluate("element => element.innerText").strip()
            if inner_text and len(inner_text) > 10:  # Partial text
                return f"text={inner_text[:10]}"
            return None

        elif selector_type.lower() == "tagname":
            tag_name = element.evaluate("element => element.tagName.toLowerCase()")
            return f"tag={tag_name}" if tag_name else None

        elif selector_type.lower() == "css selector":
            css_selector = element.evaluate("element => element.getAttribute('css')")
            return f"css={css_selector}" if css_selector else None

        elif selector_type.lower() == "xpath":
            return f"xpath={get_xpath(element)}"

    except Exception as e:
        print(f"Error getting {selector_type} for element: {e}")

    return None  # If no matching selector is found


# Main script to iterate through elements and print only the specified selector along with its text content
def main(selector_type):
    with sync_playwright() as p:
        # Connect to an active browser instance on the specified debugging port
        browser = p.chromium.connect_over_cdp("http://localhost:9214")
        default_context = browser.contexts[0]

        # Retrieve the first page in the context.
        page = default_context.pages[0]

        # Wait for the page to load fully
        page.wait_for_load_state("load")

        # Store unique selectors in a set
        unique_selectors = set()

        # Get all elements on the page
        elements = page.query_selector_all("*")

        # Retrieve the specific selector for each element based on user input
        for element in elements:
            try:
                # Get the selector based on the user-specified type
                selector = get_specific_selector(element, selector_type)
                if selector:
                    # Capture the text content of the element
                    text_content = element.evaluate("element => element.innerText").strip() or "No text"
                    # Combine selector and text content into a unique entry
                    unique_entry = f"Text: '{text_content}' - Selector: {selector}"

                    # Add to set if it's a unique entry
                    if unique_entry not in unique_selectors:
                        unique_selectors.add(unique_entry)
            except Exception as e:
                print(f"Error processing element: {e}")

        # Print all unique selectors and text content
        for entry in unique_selectors:
            print(entry)

        # Close the browser connection after processing all elements
        browser.close()


if __name__ == "__main__":
    # Specify the selector type you want to retrieve
    user_input_selector_type = "xpath"  # Replace this with any desired selector type
    main(user_input_selector_type)
