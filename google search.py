import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
searchbox=input("enter the sentence to search\n: ")
driver=webdriver.Chrome()
driver.get("https://www.google.com/")
driver.implicitly_wait(30)
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.fullscreen_window()
driver.find_element_by_name('q').send_keys(searchbox)
driver.find_element_by_name('btnK').click()
#driver.find_element_by_xpath('//input[@class="gNO89b" and @value="Google Search"]').click()
#driver.find_element_by_xpath('//a[@class="gb_d"and@data-pid="23"and@target="_top"]').click()
driver.minimize_window()
driver.close()
print("google search is success")