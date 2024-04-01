import os
import re
import subprocess
import pytest
from selenium import webdriver

def test_args():
    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get('http://selenium.dev')

    driver.quit()

# Test logging service output to a file
@pytest.fixture
def log_path(tmp_path):
    return tmp_path / "geckodriver.log"