import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#driver=webdriver.Edge(executable_path='D:\drivers\msedgedriver.exe')
driver=webdriver.Chrome("D:\drivers\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="D:\drivers\geckodriver.exe")
driver.get('https://netbanking.hdfcbank.com/netbanking/?_ga=2.176378149.1819882415.1533883212-608727520.1532670997')
time.sleep(2)
driver.find_element(By.XPATH,'//a[contains(text(),"CONTINUE")]').click()
#driver.find_elements_by_class_name("btn btn-primary login-btn").click()
