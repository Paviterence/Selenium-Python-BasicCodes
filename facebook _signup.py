import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browser=webdriver.Chrome(executable_path='D:\drivers\chromedriver.exe')
browser.maximize_window()
browser.get("https://www.facebook.com/")

print("url is:\n",browser.current_url)
time.sleep(2)
browser.find_element(By.XPATH,'//a[@data-testid="open-registration-form-button"]').click()
print("signup url is:\n",browser.current_url)
time.sleep(4)
browser.find_element(By.XPATH,'//input[@name="firstname"]').send_keys("pavithrabalan")
time.sleep(1)
browser.find_element(By.XPATH,'(//input[@type="text"])[3]').send_keys("sethu")
time.sleep(1)
browser.find_element(By.XPATH,'(//input[@type="text"])[4]').send_keys("lovelydreams1709@gmail.com")
browser.find_element(By.XPATH,'//input[@name="reg_email_confirmation__"]').send_keys("lovelydreams1709@gmail.com")
time.sleep(1)
browser.find_element(By.XPATH,'(//input[@type="password"])[2]').send_keys("pae23456dfd")

browser.find_element(By.XPATH,'//select[@aria-label="Day"]').send_keys("17")

browser.find_element(By.XPATH,'//select[@aria-label="Month"]').send_keys("may")
browser.find_element(By.XPATH,'//select[@aria-label="Year"]').send_keys("1997")
browser.find_element(By.XPATH,'(//input[@type="radio"])[2]').click()
browser.find_element(By.XPATH,'//button[text()="Sign Up"]').click()
time.sleep(5)
browser.close()