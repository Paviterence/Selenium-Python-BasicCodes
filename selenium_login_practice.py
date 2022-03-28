
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.remote_connection import RemoteConnection
#driver=webdriver.Chrome('G:\driver\chromedriver_win32\chromedriver.exe')#my pc
#driver=webdriver.Edge(executable_path='D:\drivers\msedgedriver.exe')
driver=webdriver.Chrome("D:\drivers\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="D:\drivers\geckodriver.exe")
#driver.implicitly_wait(30)
driver.get("https://www.instagram.com/")
print("1.title of insta:\n",driver.title)
print("url:\n",driver.current_url)
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath('//input[@aria-label="Phone number, username, or email"and@aria-required="true"and@name="username"]').send_keys("hi_i_pavi")
driver.find_element(By.XPATH,'//input[@aria-label="Password"and@name="password"]').send_keys("hshhdyw")
time.sleep(2)
driver.find_element(By.XPATH,'//div[contains(text(),"Log In")]').click()#text function '//div[text()="Log In")]'
time.sleep(3)
print("====done====")
print("**amazon search**")
driver.get("https://www.amazon.in/")
driver.maximize_window()
print("2.title of amazon:\n",driver.title)
print("url:\n",driver.current_url)
#driver.find_element(By.XPATH,('//input[@type="text"and@id="twotabsearchtextbox"and@aria-label="Search"]')).send_keys(searchbox)
driver.find_element_by_xpath('//input[@type="text"and@id="twotabsearchtextbox"and@aria-label="Search"]').send_keys("samsung s21 fe 5g")
time.sleep(3)
driver.find_element(By.ID,"nav-search-submit-button").click()
time.sleep(5)
print("====done====")
print("**google search**")
driver.get("https://www.google.com/")
print("3.title of google is:\n",driver.title)
print("url is:\n",driver.current_url)
driver.find_element_by_name('q').send_keys("selenium interview question")
time.sleep(3)
driver.find_element_by_name('btnK').click()
#driver.find_element_by_xpath('//input[@class="gNO89b" and @value="Google Search"]').click()
#driver.find_element_by_xpath('//a[@class="gb_d"and@data-pid="23"and@target="_top"]').click()
print("google search is success")
print("====done====")

print("**fb login**")
driver.get("https://www.facebook.com/")
title=driver.title
if title=="Facebook – log in or sign up":
    print("success")
    print("the title is",title)
else:
    print("failure")
print("4.title of facebook is:\n",title)
print("url:\n",driver.current_url)
#driver.find_element_by_id("email").send_keys(username)
driver.find_element(By.ID,"email").send_keys("pavithran")
time.sleep(3)
driver.find_element(By.ID,"pass").send_keys("ynunufwyhu")
#driver.find_element_by_id("pass").send_keys(password)
#driver.find_element_by_name("login")
driver.find_element(By.NAME,"login").click()
time.sleep(5)
print("====done====")
print("**youtube search**")
driver.get('https://www.youtube.com')
print("5.title of youtube is:\n",driver.title)
print("url:\n",driver.current_url)
driver.fullscreen_window()
driver.find_element_by_xpath('//input[@id="search"and@name="search_query"and @tabindex="0"and@type="text"]').send_keys("arabic kuthu song")
time.sleep(2)
driver.find_element_by_xpath('//button[@id="search-icon-legacy"and @class="style-scope ytd-searchbox"and @aria-label="Search"]').click()
time.sleep(5)
driver.quit()





