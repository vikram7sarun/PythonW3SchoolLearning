import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://acme-test.uipath.com/login")
    page.get_by_label("Email:").click()
    page.get_by_label("Email:").fill("vikic3110@gmail.com")
    page.get_by_label("Password:").fill("Test@123")
    page.get_by_role("button", name="Login").click()

    page1 = context.new_page()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
