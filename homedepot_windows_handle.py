import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
search=input("what you want\n:")
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.homedepot.com/")
print(driver.title)
wait=WebDriverWait(driver,10)
searchbox=wait.until(ec.presence_of_element_located((By.ID,'headerSearch')))
searchbox.send_keys(search,Keys.ENTER)
time.sleep(3)
clickele=driver.find_element(By.XPATH,'//div[@class="product-pod__title product-pod__title__product"]')
clickele.click()
currentwindow=driver.current_window_handle
print(currentwindow)
# windowid=driver.window_handles
# print("windows id below here\n:",windowid)
# driver.switch_to.window(windowid[1])
# print("additional window titrl\n",driver.title)
addto_cart=wait.until(ec.presence_of_element_located((By.XPATH,'//button[@class="bttn bttn--primary"]')))
addto_cart.click()
time.sleep(5)
driver.close()
# driver.switch_to.window(currentwindow)
# print(driver.title)
# time.sleep(3)
# driver.quit()