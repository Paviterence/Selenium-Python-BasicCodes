import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
search=input("what you want\n:")
s=Service(executable_path='D:\drivers\chromedriver.exe')
driver = webdriver.Chrome(service=s)
# driver=webdriver.Chrome(executable_path='D:\drivers\chromedriver.exe')
driver.maximize_window()
driver.get("https://www.snapdeal.com/")
print(driver.title)
print(driver.current_url)
wait=WebDriverWait(driver,10)
searchbox=wait.until(ec.presence_of_element_located((By.XPATH,'//input[@id="inputValEnter"]')))
searchbox.send_keys(search,Keys.ENTER)
time.sleep(2)
# driver.find_element(By.XPATH,"//*[text()='Shop ']").click()
clickele=driver.find_element(By.XPATH,'(//p[@class="product-title"])[1]')
clickele.click()

currentwindow=driver.current_window_handle
print(currentwindow)
windowid=driver.window_handles
print("windowsid below here\n",windowid)
driver.switch_to.window(windowid[1])
print("additional window titrl\n",driver.title)
addto_cart=wait.until(ec.presence_of_element_located((By.ID,"buy-button-id")))
addto_cart.click()
time.sleep(5)
driver.close()
driver.switch_to.window(currentwindow)
print(driver.title)
time.sleep(3)
driver.quit()
