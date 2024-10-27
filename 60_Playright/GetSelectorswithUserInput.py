from playwright.sync_api import sync_playwright


# Helper function to build XPath for an element
def get_xpath(element):
    path = []
    while True:
        tag_name = element.evaluate("element => element.tagName.toLowerCase()")

        # Use JavaScript to get the parent element
        parent_handle = element.evaluate_handle("element => element.parentElement")
        parent = parent_handle.as_element()  # Convert JSHandle to ElementHandle

        if parent:  # If there's a parent element
            # Get siblings of the same tag within the parent
            siblings = parent.query_selector_all(tag_name)
            index = siblings.index(element) + 1 if len(siblings) > 1 else 0
            path.append(f"{tag_name}{f'[{index}]' if index > 0 else ''}")

            # Move up to the parent for the next iteration
            element = parent
        else:
            path.append(tag_name)
            break

        # Release the JSHandle to free up memory
        parent_handle.dispose()

    return "/" + "/".join(reversed(path))


# Function to find a specific type of selector
def get_specific_selector(element, selector_type):
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

    return None  # If no matching selector is found


# Main script to iterate through elements and print only the specified selector
def main(selector_type):
    with sync_playwright() as p:
        # Connect to an active browser instance on the specified debugging port
        browser = p.chromium.connect_over_cdp("http://localhost:9214")
        default_context = browser.contexts[0]

        # Retrieve the first page in the context.
        page = default_context.pages[0]

        # Get all elements on the page
        elements = page.query_selector_all("*")

        # Retrieve the specific selector for each element based on user input
        for element in elements:
            selector = get_specific_selector(element, selector_type)
            if selector:  # Only print if the selector is found
                tag_name = element.evaluate("element => element.tagName.toLowerCase()")
                print(f"Selector for element ({tag_name}): {selector}")

        # Close the browser connection
        browser.close()


if __name__ == "__main__":
    # Specify the selector type you want to retrieve
    user_input_selector_type = "tagname"  # Replace this with any desired selector type
    main(user_input_selector_type)
