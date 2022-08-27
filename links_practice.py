import time

import  selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.get('http://demo.automationtesting.in/Index.html')
driver.find_element(By.ID,"email").send_keys()
driver.find_element(By.ID,'enterimg').click()
print('title is:',driver.title)
print('url is :',driver.current_url)
time.sleep(2)
links=driver.find_elements(By.TAG_NAME,'a')
total_links=len(links)
print("total links present in the websites:",total_links)
for i in links:
    print((i.text))
#driver.find_element(By.LINK_TEXT,"Widgets").click()
driver.find_element(By.PARTIAL_LINK_TEXT,'gets').click()
time.sleep(5)
driver.quit()