from playwright.sync_api import sync_playwright


# Helper function to build a selector based on priority
def get_priority_selector(element):
    # Prioritize based on ID, Name, ClassName, LinkText, Partial LinkText, TagName, CSS Selector
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
        print(f"Error generating selector for element: {e}")

    return None  # If no matching attribute found for selector


# Main script to iterate through elements and print unique selectors in priority order
def main():
    with sync_playwright() as p:
        # Connect to an active browser instance on the specified debugging port
        browser = p.chromium.connect_over_cdp("http://localhost:9214")
        default_context = browser.contexts[0]

        # Retrieve the first page in the context.
        page = default_context.pages[0]

        # Wait for the page to load fully
        page.wait_for_load_state("load")

        # Dictionaries to store selectors based on their priority
        selectors_by_priority = {
            "ID": [],
            "Name": [],
            "ClassName": [],
            "LinkText": [],
            "PartialLinkText": [],
            "TagName": [],
            "CSSSelector": []
        }

        # Get all elements on the page
        elements = page.query_selector_all("*")

        # Retrieve a single selector for each element based on priority
        for element in elements:
            try:
                # Generate a single selector based on priority
                selector = get_priority_selector(element)

                # Classify selector based on priority
                if selector and "id=" in selector:
                    selectors_by_priority["ID"].append(selector)
                elif selector and "name=" in selector:
                    selectors_by_priority["Name"].append(selector)
                elif selector and "contains(@class," in selector:
                    selectors_by_priority["ClassName"].append(selector)
                elif selector and "text()=" in selector:
                    selectors_by_priority["LinkText"].append(selector)
                elif selector and "contains(text()," in selector:
                    selectors_by_priority["PartialLinkText"].append(selector)
                elif selector and selector.startswith("//"):
                    selectors_by_priority["TagName"].append(selector)
                elif selector:
                    selectors_by_priority["CSSSelector"].append(selector)

            except Exception as e:
                print(f"Error processing element: {e}")

        # Print selectors based on priority
        for priority in ["ID", "Name", "ClassName", "LinkText", "PartialLinkText", "TagName", "CSSSelector"]:
            for selector in selectors_by_priority[priority]:
                print(selector)

        # Close the browser connection after processing all elements
        browser.close()


if __name__ == "__main__":
    main()
