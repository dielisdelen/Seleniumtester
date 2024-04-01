from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options = Options()
options.headless = True
service = Service(executable_path='/usr/local/bin/geckodriver', log_path='procesverloop/Seleniumtester/logs/geckodriver.log')
service.start()

driver = webdriver.Firefox(service=service, options=options)

# Navigate to a website and print its title
try:
    driver.get("http://nu.nl")
    print(driver.title)
finally:
    driver.quit()