#cd C:\Program Files\Google\Chrome\Application
#chrome.exe --remote-debugging-port=9214 --no-first-run --no-default-browser-check --user-data-dir="C:\ChromeData"

# Import the sync_playwright function from the sync_api module of Playwright.
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
# Start a new session with Playwright using the sync_playwright function.
with sync_playwright() as playwright:
    # Connect to an existing instance of Chrome using the connect_over_cdp method.
    browser = playwright.chromium.connect_over_cdp("http://localhost:9214")

    # Retrieve the first context of the browser.
    default_context = browser.contexts[0]

    # Retrieve the first page in the context.
    page = default_context.pages[0]

    page.goto("https://acme-test.uipath.com/")

    # page = browser.pages[0]  # Access the active page

    # Extract and print all selectors (or specific selectors as needed)
    elements = page.query_selector_all("*")
    for element in elements:
        print(element.evaluate("element => element.outerHTML"))

