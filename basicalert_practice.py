import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
driver=webdriver.Firefox()
driver.implicitly_wait(30)
driver.get('https://www.rediffmailpro.com/cgi-bin/login.cgi')
print("Tittle is:",driver.title)
print("url is:",driver.current_url)
driver.find_element(By.XPATH,'//input[@type="submit"and@class="vmiddle"]').click()
alert=driver.switch_to.alert
print("the  alert text here:",alert.text)
time.sleep(2)
alert.accept()

time.sleep(2)
driver.close()

