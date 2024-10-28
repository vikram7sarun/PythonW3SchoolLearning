def convert_selectors_to_dict(selectors):
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

        # Add the selector dictionary to the elements list
        elements.append({
            'name': name,
            'type': 'xpath',
            'locator': selector
        })
    return elements

# Example usage
selectors = [
    "//*[@id='password']",
    "//*[@id='email']",
    "//*[@id='remember']",
    "//*[@id='bs-example-navbar-collapse-1']",
    "//*[@name='_token']",
    "//*[@name='csrf-token']",
    "//*[@name='viewport']",
    "//*[contains(@class, 'control-group') and contains(@class, 'form-group')]",
    "//*[contains(@class, 'breadcrumb')]",
    "//*[contains(@class, 'navbar-toggle')]",
    "//*[contains(@class, 'row')]",
    "//*[contains(@class, 'form-group') and contains(@class, 'control-group')]",
    "//*[contains(@class, 'col-lg-12')]",
    "//*[contains(@class, 'btn') and contains(@class, 'bg-warning')]",
    "//*[contains(@class, 'sr-only')]",
    "//*[contains(@class, 'navbar-brand')]",
    "//*[contains(@class, 'navbar-header')]",
    "//*[contains(@class, 'form-check-label')]",
    "//*[contains(@class, 'controls')]",
    "//*[contains(@class, 'btn') and contains(@class, 'btn-primary')]",
    "//*[contains(@class, 'breadcrumb-item') and contains(@class, 'active')]",
    "//*[contains(@class, 'col-md-6')]",
    "//*[contains(@class, 'nav') and contains(@class, 'navbar-nav') and contains(@class, 'navbar-right')]",
    "//*[contains(@class, 'breadcrumb-item')]",
    "//*[contains(@class, 'container')]",
    "//*[contains(@class, 'icon-bar')]",
    "//*[contains(@class, 'controls') and contains(@class, 'form-check')]",
    "//*[contains(@class, 'page-header')]",
    "//*[contains(@class, 'navbar') and contains(@class, 'navbar-inverse') and contains(@class, 'navbar-fixed-top')]",
    "//*[contains(@class, 'main-container')]",
    "//*[text()='Log In']",
    "//*[text()='Email:']",
    "//*[text()='Password:']",
    "//*[text()='Home']",
    "//*[contains(text(), 'ACME Syste')]",
    "//*[contains(text(), 'To continu')]",
    "//*[contains(text(), 'Switch to ')]",
    "//*[contains(text(), 'new Date()')]",
    "//*[contains(text(), 'Email')]",
    "//*[contains(text(), 'Copyright ')]"
]

elements = convert_selectors_to_dict(selectors)
print(elements)