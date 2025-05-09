import os
from pathlib import Path

from playwright.sync_api import sync_playwright

Selenium_user_data_dir = os.environ.get("SELENIUM_USER_DATA_DIR")


def screenshot(url: str, file_path: Path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()

        page = context.new_page()
        page.goto(url, wait_until="load")
        page.wait_for_timeout(5000)

        # Handle the cookie consent/email popup
        try:
            page.wait_for_selector("#cta-close", timeout=10000)
            page.click("#cta-close")
        except Exception:
            pass  # If the button doesn't appear, continue

        page.screenshot(path=str(file_path), full_page=True)
        context.close()
        browser.close()
