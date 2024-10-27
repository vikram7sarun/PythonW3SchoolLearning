from playwright.sync_api import sync_playwright


# Helper function to build XPath for an element
def get_xpath(element):
    path = []
    while element:
        tag_name = element.evaluate("element => element.tagName.toLowerCase()")
        siblings = element.parent_element.query_selector_all(tag_name) if element.parent_element else []
        index = siblings.index(element) + 1 if len(siblings) > 1 else 0
        path.append(f"{tag_name}{f'[{index}]' if index > 0 else ''}")
        element = element.parent_element
    return "/" + "/".join(reversed(path))


# Function to find selectors based on priority
def get_priority_selector(element):
    # Check for ID
    element_id = element.evaluate("element => element.id")
    if element_id:
        return f"id={element_id}"

    # Check for Name
    name_attr = element.evaluate("element => element.getAttribute('name')")
    if name_attr:
        return f"name={name_attr}"

    # Check for ClassName
    class_attr = element.evaluate("element => element.className")
    if class_attr:
        class_name = ".".join(class_attr.split())
        return f"class={class_name}"

    # Check for LinkText or Partial LinkText if it has inner text
    inner_text = element.evaluate("element => element.innerText").strip()
    if inner_text:
        if len(inner_text) <= 10:  # Exact match if text is short
            return f"text={inner_text}"
        else:  # Partial match for longer texts
            return f"text={inner_text[:10]}"

    # Use TagName
    tag_name = element.evaluate("element => element.tagName.toLowerCase()")
    if tag_name:
        return f"tag={tag_name}"

    # Check CSS Selector
    css_selector = element.evaluate("element => element.getAttribute('css')")
    if css_selector:
        return f"css={css_selector}"

    # Fallback to XPath if none of the above applies
    return f"xpath={get_xpath(element)}"


# Main script to iterate through elements and print selectors
def main():
    with sync_playwright() as p:
        # Connect to an active browser instance on the specified debugging port
        browser = p.chromium.connect_over_cdp("http://localhost:9214")
        default_context = browser.contexts[0]

        # Retrieve the first page in the context.
        page = default_context.pages[0]
        # page = browser.pages[0]

        # Get all elements on the page
        elements = page.query_selector_all("*")

        # Retrieve selectors based on priority and print them
        for element in elements:
            selector = get_priority_selector(element)
            tag_name = element.evaluate("element => element.tagName.toLowerCase()")
            print(f"Selector for element ({tag_name}): {selector}")

        # Close the browser connection
        browser.close()


if __name__ == "__main__":
    main()
