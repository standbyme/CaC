import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Selenium_user_data_dir = os.environ.get("SELENIUM_USER_DATA_DIR")


def screenshot(url: str, file_path: Path):
    options = Options()
    if Selenium_user_data_dir:
        options.add_argument(f"user-data-dir={Selenium_user_data_dir}")

    options.add_argument("--headless")
    options.add_argument("profile-directory=Selenium")

    driver = webdriver.Firefox(options=options)

    driver.get(url)
    driver.implicitly_wait(20)

    # [Key] Handle the cookie consent/email popup
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.ID, "cta-close")))
    button.click()

    driver.get_full_page_screenshot_as_file(str(file_path))
