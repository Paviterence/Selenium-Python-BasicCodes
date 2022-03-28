#explicit wait its completely based on the condition
#its always looks for particular element for ebery element wee need to give the conditions
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome(executable_path='D:\drivers\chromedriver.exe')
driver.implicitly_wait(5)
driver.get('https://www.redbus.com/')
element=WebDriverWait(driver,5).until(Ec.element_to_be_clickable((By.XPATH,'//button[text()="Accept All"]')))
element.click()
# driver.find_element(By.XPATH,'//button[text()="Accept All"]').click()
#driver.find_element(By.ID,"src").send_keys("chennai")
ele=WebDriverWait(driver,5).until(Ec.presence_of_element_located((By.ID,'src')))
ele.send_keys("chennai")
ele_2=WebDriverWait(driver,5).until(Ec.presence_of_element_located((By.ID,'dest')))
ele_2.send_keys("karaikudi")
time.sleep(2)
driver.find_element(By.XPATH,'//div[@class="fl search-box date-box gtm-onwardCalendar"]').click()
driver.find_element(By.XPATH,"//label[normalize-space()='Onward Date']").send_keys('22-Mar-2022')
# driver.find_element(By.XPATH,'//div[@class="fl search-box date-box gtm-returnCalendar"]').send_keys('22-Mar-2022')