import selenium
import time
from time import sleep
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import  By
#from webdriver_manager.chrome import  ChromeDriver
#from selenium.webdriver.support.ui import WebDriverWait
#import selenium_browser
# driver=webdriver.Chrome(executable_path="D:\drivers\chromedriver.exe")
# driver=webdriver.Firefox(executable_path="D:\drivers\geckodriver.exe")
#driver=webdriver.Edge(executable_path="D:\drivers\msedgedriver")
# s=Service(executable_path='D:\drivers\chromedriver.exe')
# driver = webdriver.Chrome(service=s)
'''to find x path just go to the website click inspect element and choose the tab
then press ctrl+f then type to conform the xpath incase if you found id or name 1st preference is given to them
the code is example
if you inspect serach bar or tab the code start like is = //input[@name="search"] like this
there is no id or name we need to verify that so proceed this method
//input[@type="submit" and @value="login"]
links
//a[text()='content']
//a[contains(text(),'content')]
for button:
'''