from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument('--no-sandbox')  # Bypass OS security model, REQUIRED on Linux if running as root
options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems

driver = webdriver.Chrome(options=options)
driver.get('https://www.example.com')

print(driver.title)
driver.quit()