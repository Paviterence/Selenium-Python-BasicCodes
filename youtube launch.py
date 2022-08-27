import selenium
import time
from time import sleep
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import  By
#from webdriver_manager.chrome import  ChromeDriver
#import selenium_browser
from selenium.webdriver.common.by import By

searchbox=input("what you want from youtube\n:")
driver=webdriver.Chrome()
#driver=webdriver.Firefox(executable_path="D:\drivers\geckodriver.exe")
#driver=webdriver.Edge(executable_path='D:\drivers\msedgedriver.exe')
driver.get('https://www.youtube.com')
driver.implicitly_wait(30)
print(driver.current_url)
driver.maximize_window()
driver.find_element_by_xpath('//input[@id="search"and@name="search_query"and @tabindex="0"and@type="text"]').send_keys(searchbox)
time.sleep(5)
driver.find_element_by_xpath('//button[@id="search-icon-legacy"and @class="style-scope ytd-searchbox"and @aria-label="Search"]').click()
driver.find_element(By.ID,'thumbnail').click()
time.sleep(5)
#driver.quit()