def convert_selectors_to_dict(selectors):
    elements = []
    for selector in selectors:
        # Default name in case extraction fails
        name = "custom_selector"

        # Check for text equality or contains function in XPath and extract accordingly
        if "text()='" in selector:
            name_part = selector.split("text()='")[1].split("']")[0]
        elif "contains(text()," in selector:
            name_part = selector.split("contains(text(), '")[1].split("')")[0]
        else:
            name_part = "unknown"

        # Generate name by formatting the extracted text
        name = name_part.lower().replace(" ", "_").replace(":", "")

        # Add the selector dictionary to the elements list
        elements.append({
            'name': f"{name}",
            'type': 'xpath',
            'locator': selector
        })
    return elements


# Example usage
selectors = [
    "//*[text()='Home']",
    "//*[text()='Password:']",
    "//*[text()='Log In']",
    "//*[text()='Email:']",
    "//*[contains(text(), 'To continu')]",
    "//*[contains(text(), 'ACME Syste')]"
]

elements = convert_selectors_to_dict(selectors)
print(elements)
