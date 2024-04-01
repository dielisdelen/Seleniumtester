from selenium import webdriver

options = webdriver.FirefoxOptions()

options.add_argument("-headless")

driver = webdriver.Firefox(options=options)

# Navigate to a website and print its title
try:
    driver.get("http://google.com")
    print(driver.title)
finally:
    driver.quit()
