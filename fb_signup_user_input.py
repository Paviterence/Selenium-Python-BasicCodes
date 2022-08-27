import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
fname=input("enter the first name:\n")
lname=input("enter the surname:\n")
mobile=input("enter the mobile number or email:\n")
passcode=input("enter the password:\n")
date=int(input("enter the date:\n"))
month=str(input("enter the month:\n"))
year=int(input("enter the year:\n"))
sex=str(input("Enter the sex female or male or custom:\n"))

browser=webdriver.Chrome()
browser.get("https://www.facebook.com/")
browser.maximize_window()
print("url is:\n",browser.current_url)
time.sleep(2)
browser.find_element(By.XPATH,'//a[@data-testid="open-registration-form-button"]').click()
print("signup url is:\n",browser.current_url)
time.sleep(4)
browser.find_element(By.XPATH,'//input[@name="firstname"]').send_keys(fname)
time.sleep(1)
browser.find_element(By.XPATH,'(//input[@type="text"])[3]').send_keys(lname)
time.sleep(1)
browser.find_element(By.XPATH,'(//input[@type="text"])[4]').send_keys(mobile)
time.sleep(2)
browser.find_element(By.XPATH,'//input[@name="reg_email_confirmation__"]').send_keys(mobile)

time.sleep(1)
browser.find_element(By.XPATH,'(//input[@type="password"])[2]').send_keys(passcode)

browser.find_element(By.XPATH,'//select[@aria-label="Day"]').send_keys(date)

browser.find_element(By.XPATH,'//select[@aria-label="Month"]').send_keys(month)
browser.find_element(By.XPATH,'//select[@aria-label="Year"]').send_keys(year)
if sex=="female":
    browser.find_element(By.XPATH, '(//input[@type="radio"])[1]').click()
elif sex=="male":
    browser.find_element(By.XPATH, '(//input[@type="radio"])[2]').click()
else:
    browser.find_element(By.XPATH, '(//input[@type="radio"])[3]').click()

browser.find_element(By.XPATH,'//button[text()="Sign Up"]').click()
#time.sleep(5)
#browser.close()