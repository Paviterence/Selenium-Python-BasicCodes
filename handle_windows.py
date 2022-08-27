import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
search=input("what you want from amazon\n:")
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
print((driver.title))
print(driver.current_url)
wait=WebDriverWait(driver,5)
searchbox=wait.until(ec.presence_of_element_located((By.ID,'twotabsearchtextbox')))
searchbox.send_keys(search,Keys.ENTER)
# driver.find_element(By.XPATH,"//*[text()='Shop ']").click()
element_click=wait.until(ec.element_to_be_clickable((By.XPATH,'(//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"and@target="_blank"])[1]')))
element_click.click()

parentwindow=driver.current_window_handle
print(parentwindow)
windowid=driver.window_handles
print("windowsid below here\n",windowid)
driver.switch_to.window(windowid[1])
print("additional window titrl\n",driver.title)
addto_cart=wait.until(ec.presence_of_element_located((By.ID,'add-to-cart-button')))
addto_cart.click()
time.sleep(5)
driver.close()
driver.switch_to.window(parentwindow)
print(driver.title)
time.sleep(3)
driver.quit()
