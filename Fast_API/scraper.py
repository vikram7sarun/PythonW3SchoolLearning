from playwright.sync_api import sync_playwright
from lxml import etree
from typing import Dict, List


def capture_selectors(element) -> Dict[str, str]:
    """
    Capture all priority selectors for a given element and generate a dynamic XPath.
    """
    selectors = {}

    # Capture ID (if exists)
    if element.get("id"):
        selectors["id"] = element.get("id")

    # Capture Name (if exists)
    if element.get("name"):
        selectors["name"] = element.get("name")

    # Capture Class (if exists)
    class_attr = element.get("class")
    if class_attr:
        selectors["class"] = class_attr.split()  # Classes are space-separated

    # Capture Tag
    selectors["tag"] = element.tag

    # Generate a dynamic XPath based on attributes
    attributes = [f"@{attr}='{element.get(attr)}'" for attr in element.keys() if element.get(attr)]
    if attributes:
        selectors["xpath"] = f"//{element.tag}[{' and '.join(attributes)}]"
    else:
        selectors["xpath"] = f"//{element.tag}"

    return selectors


def scrape_active_tab_with_playwright() -> Dict[str, List[Dict[str, str]]]:
    """
    Use Playwright to connect via remote debugging, fetch the active tab, and scrape elements.
    """
    try:
        with sync_playwright() as p:
            # Connect to Chrome via remote debugging
            browser = p.chromium.connect_over_cdp("http://localhost:9214")

            # Access the active tab
            context = browser.contexts[0]
            if not context.pages:
                raise Exception("No active tabs found in the browser.")

            page = context.pages[0]
            url = page.url
            print(f"Active tab URL: {url}")

            # Get page content
            html_content = page.content()

            # Parse the HTML
            tree = etree.HTML(html_content)
            functional_elements = tree.xpath("//button | //input")  # Find buttons and inputs

            # Extract selectors for each element
            elements_data = [capture_selectors(el) for el in functional_elements]

            return {
                "url": url,
                "elements": elements_data
            }
    except Exception as e:
        print(f"Error during scraping: {str(e)}")
        raise Exception(f"Scraping failed: {str(e)}")