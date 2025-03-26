from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
service=Service(r"C:\Users\monishasundar\Downloads\Chromedriver\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(3)
suggestion=driver.find_element(By.XPATH,'//*[@id="autocomplete"]')
suggestion.click()
suggestion.send_keys("india")
time.sleep(10)

