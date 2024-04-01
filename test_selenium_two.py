import os
import subprocess
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

# Test running Firefox in headless mode
def test_arguments():
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")  # Run in headless mode

    driver = webdriver.Firefox(options=options)
    driver.get("https://www.nu.nl")  # Open a website to verify headless mode works
    assert "Example Domain" in driver.title  # Simple assertion to check the page title
    driver.quit()

# Test logging service output to a file
@pytest.fixture
def log_path(tmp_path):
    return tmp_path / "geckodriver.log"

def test_log_to_file(log_path):
    service = FirefoxService(log_path=str(log_path), service_args=['--log', 'debug'])

    driver = webdriver.Firefox(service=service)
    driver.get("https://www.selenium.dev")  # Navigate to a page

    # Check the log file for a specific log entry to verify logging works
    with open(log_path, 'r') as fp:
        log_content = fp.read()
        assert "geckodriver	INFO	Listening on" in log_content

    driver.quit()
