import selenium
from selenium import webdriver
#from selenium.webdriver.common.by import  By
#driver=webdriver.Chrome("D:\drivers\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="D:\drivers\geckodriver.exe")
driver=webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
print(driver.page_source)
print(driver.title)
print(driver.current_url)
driver.close()

