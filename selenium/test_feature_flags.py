from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    driver.get("http://127.0.0.1:5001")

    assert "Feature Flag Demo" in driver.title
    assert "new_dashboard" in driver.page_source
    assert "dark_mode" in driver.page_source
    assert "beta_feature" in driver.page_source

    print("PASS: Feature Flag Demo loaded successfully")
    print("PASS: All three feature flags are displayed")

finally:
    driver.quit()
