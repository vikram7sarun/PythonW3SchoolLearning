from playwright.sync_api import sync_playwright


# Helper function to build a selector based on priority
def get_priority_selector(element):
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

        # Check for LinkText (exact match for short text)
        inner_text = element.evaluate("element => element.innerText").strip() if element.evaluate(
            "element => element.innerText") else ""
        if inner_text and len(inner_text) <= 10:
            return f"//*[text()='{inner_text}']"

        # Check for Partial LinkText (longer texts)
        if inner_text and len(inner_text) > 10:
            return f"//*[contains(text(), '{inner_text[:10]}')]"

        # Use TagName if nothing else matches
        tag_name = element.evaluate("element => element.tagName.toLowerCase()")
        if tag_name:
            return f"//{tag_name}"

    except Exception as e:
        print(f"Error generating selector for element: {e}")

    # Return None if no match found
    return None


# Main script to iterate through elements and print unique selectors based on user input
def main():
    # Get user input for desired selector priorities
    print("Enter the desired selector priorities (e.g., ID, Name, ClassName, LinkText, PartialLinkText, TagName):")
    user_input = input("Priorities (comma-separated): ").split(",")
    desired_priorities = [priority.strip() for priority in user_input]

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9214")
        default_context = browser.contexts[0]
        page = default_context.pages[0]
        page.wait_for_load_state("load")

        # Dictionaries to store selectors based on their priority
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

                # Classify selector based on priority
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

        # Print selectors based on user-defined priorities
        for priority in desired_priorities:
            if priority in selectors_by_priority:
                print(f"\n{priority} Selectors:")
                for selector in selectors_by_priority[priority]:
                    print(selector)
            else:
                print(f"\nNo selectors found for priority: {priority}")

        browser.close()


if __name__ == "__main__":
    main()
