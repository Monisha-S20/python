# from selenium import webdriver
# import time
# Specify the path to chromedriver using 'executable_path'
# driver = webdriver.Chrome(executable_path=r"C:/Users/monishasundar/Downloads/Chromedriver/chromedriver-win64/chromedriver.exe")

# Open a webpage (example)
# driver.get("https://www.google.com")
# time.sleep(50)

# Close the browser after use
# driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Specify the path to chromedriver using the Service class
# r is a raw string if it is used for avoid the //slash issue
service = Service(r"C:/Users/monishasundar/Downloads/Chromedriver/chromedriver-win64/chromedriver.exe")

# Initialize WebDriver with the service object
driver = webdriver.Chrome(service=service)

# Now you can perform actions with the WebDriver
driver.get("https://www.google.com")

time.sleep(10)

# Close the browser after use
driver.quit()

