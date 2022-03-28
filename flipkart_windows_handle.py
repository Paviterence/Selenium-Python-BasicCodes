from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.service import Service
# s=Service('D:\drivers\chromedriver.exe')
# driver = webdriver.Chrome(service=s)
driver=webdriver.Chrome(executable_path='D:\drivers\chromedriver.exe')
driver.get("https://www.flipkart.com/")
time.sleep(2)
driver.maximize_window()
print(driver.current_url)
wait=WebDriverWait(driver,10)
#below code for remove the login alert
close=wait.until(ec.element_to_be_clickable((By.XPATH,'//button[@class="_2KpZ6l _2doB4z"]')))
close.click()
#finding the search box
#for redmi
search_box=wait.until(ec.presence_of_element_located((By.XPATH,'//input[@class="_3704LK"and@name="q"]')))
search_box.clear()
search_box.send_keys("remi phone",Keys.ENTER)
click_element=wait.until(ec.element_to_be_clickable((By.XPATH,'(//div[@class="_4rR01T"])[1]')))
click_element.click()
parentwindow=driver.current_window_handle
print(parentwindow)
windowid=driver.window_handles
print("windows id\n:",windowid)
driver.switch_to.window(windowid[1])
price=wait.until(ec.presence_of_element_located((By.XPATH,'//div[@class="_30jeq3 _16Jk6d"]')))
print("price of redmi phone:",price.text)
driver.close()
driver.switch_to.window(parentwindow)
search_box.clear()
driver.back()
time.sleep(5)
#for mask
search_box.send_keys("mask",Keys.ENTER)
click_element=wait.until(ec.element_to_be_clickable((By.XPATH,'(//a[@class="s1Q9rs"])[2]')))
click_element.click()
windowid=driver.window_handles
print("windows id\n:",windowid)
driver.switch_to.window(windowid[1])
pincode=wait.until(ec.presence_of_element_located((By.XPATH,'//input[@id="pincodeInputId"and@placeholder="Enter Delivery Pincode"]')))
pincode.send_keys("600044")
time.sleep(5)
driver.close()
driver.switch_to.window(parentwindow)
driver.back()
time.sleep(5)
#for laptop
search_box.send_keys("laptop",Keys.ENTER)
click_element=wait.until(ec.element_to_be_clickable((By.XPATH,'(//div[@class="_4rR01T"])[1]')))
click_element.click()
windowid=driver.window_handles
print("windows id\n:",windowid)
driver.switch_to.window(windowid[1])
price=wait.until(ec.presence_of_element_located((By.XPATH,'//div[@class="_30jeq3 _16Jk6d"]')))
print(price.text)
time.sleep(5)
driver.close()
driver.quit()
