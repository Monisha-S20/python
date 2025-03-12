from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service=Service(r"C:/Users/monishasundar/Downloads/Chromedriver/chromedriver-win64/chromedriver.exe")

driver=webdriver.Chrome(service=service)

try:
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
finally:
    time.sleep(3)

entertext=driver.find_element(By.NAME,"username")
entertext.send_keys("Admin")
time.sleep(3)

anothertext=driver.find_element(By.NAME,"password")
anothertext.send_keys("admin123")
time.sleep(3)

clickbroswer=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
clickbroswer.click()
time.sleep(10)

driver.quit()