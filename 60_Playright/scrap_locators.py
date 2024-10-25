from playwright.sync_api import sync_playwright

def scrape_page():
    # Start Playwright
    with sync_playwright() as p:
        # Launch a browser (you can use 'firefox' or 'webkit' instead of 'chromium')
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to a webpage
        page.goto("https://example.com")  # Replace with the URL of the page you want to scrape

        # Scrape elements by CSS selectors or XPath
        # Example 1: CSS selector for h1 tag
        h1_element = page.query_selector('h1')
        print("H1 Text:", h1_element.text_content())

        # Example 2: CSS selector for a class
        class_elements = page.query_selector_all('.example-class')
        for element in class_elements:
            print("Class element:", element.text_content())

        # Example 3: Using XPath to scrape elements
        xpath_elements = page.locator("//div[@id='example-id']")
        for element in xpath_elements.element_handles():
            print("XPath element:", element.text_content())

        # Close the browser
        browser.close()

if __name__ == "__main__":
    scrape_page()