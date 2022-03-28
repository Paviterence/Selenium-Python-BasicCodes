import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import  By
from webdriver_manager.chrome import  ChromeDriver
from selenium.webdriver.support.ui import WebDriverWait


username =input("enter username or phonenumber:")
password =input("enter the password:")

driver = webdriver.Chrome("D:\drivers\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.implicitly_wait(30)
title=driver.title
if title=="Facebook – log in or sign up":
    print("success")
    print("the title is",title)
else:
    print("failure")
#driver.find_element_by_id("email").send_keys(username)
driver.find_element(By.ID,"email").send_keys(username)
driver.find_element(By.ID,"pass").send_keys(password)
#driver.find_element_by_id("pass").send_keys(password)
#driver.find_element_by_name("login")
driver.find_element(By.NAME,"login").click()
time.sleep(5)
driver.close()

