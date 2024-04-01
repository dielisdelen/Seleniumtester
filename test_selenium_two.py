from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options = Options()
options.headless = True
service = Service(executable_path='/path/to/geckodriver', log_path='/path/to/geckodriver.log')
service.start()

driver = webdriver.Firefox(service=service, options=options)

# Navigate to a website and print its title
try:
    driver.get("http://nu.nl")
    print(driver.title)
finally:
    driver.quit()