import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
#driver=webdriver.Chrome('G:\driver\chromedriver_win32\chromedriver.exe')#mypc
driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.get('http://demo.automationtesting.in/Index.html')
driver.maximize_window()
tb1=driver.find_element(By.ID,"email")
print("displayed--->",tb1.is_displayed())
print("enabled--->",tb1.is_enabled())
tb1.send_keys("hello i am in")
time.sleep(2)
driver.find_element(By.ID,"enterimg").click()
time.sleep(2)
driver.find_element(By.XPATH,'//input[@ng-model="FirstName"]').send_keys("pavithrabalan")
driver.find_element(By.XPATH,'//input[@ng-model="LastName"]').send_keys("sethu")
time.sleep(2)
tb2=driver.find_element(By.XPATH,'//*[@ng-model="Adress"]')
print("--adress--")
print("displayed--->",tb2.is_displayed())
print("enabled--->",tb2.is_enabled())
tb2.send_keys("chrompet,chennai")
driver.find_element(By.XPATH,'//*[@ng-model="EmailAdress"]').send_keys("abc@gdsgmail.com")
driver.find_element(By.XPATH,'//input[@ng-model="Phone"]').send_keys("9874563215")
time.sleep(2)
rd1=driver.find_element(By.XPATH,'//input[@type="radio"and@ng-model="radiovalue"and@value="Male"]')
# print("male button is slected-->",rd1.is_selected())
# rd1.select()
rd1_1=print("male button is slected-->",rd1.is_selected())
if rd1_1=="True":
    print("no need to select female button")
else:
    print("select female button")
    rd2=driver.find_element(By.XPATH,'//input[@type="radio"and@ng-model="radiovalue"and@value="FeMale"]')
    rd2.click()
    print("female buton is selected--->",rd2.is_selected())
time.sleep(2)
cb1=driver.find_element(By.ID,'checkbox1')
cb1_1=print("hobbies selected",cb1.is_selected())
cb1.click()
cbl1=print("cricket selected",cb1.is_selected())
time.sleep(2)
cb2=driver.find_element(By.ID,'checkbox2')
cb2_2=print("movie selected",cb2.is_selected())
cb2.click()
cbl=print("movie selected",cb2.is_selected())
time.sleep(2)

# driver.execute_script("window.scrollby(0,1000)","")# #language
language=driver.find_element(By.XPATH,'//div[@class="ui-autocomplete-multiselect ui-state-default ui-widget"]')
language.click()
time.sleep(2)
print("==language lists==")
dropdownlist=driver.find_elements(By.CSS_SELECTOR,'li.ng-scope')
for ele in dropdownlist:
    print(ele.text)
time.sleep(4)
for ele in dropdownlist:
    print(ele.text)
    if ele.text =='English':
        ele.click()
        break
# def selectvalues(ele_list,value):
#     for ele in dropdownlist:
#         print(ele.text)
#         if ele.text == value:
#             ele.click()
#             break
#
# language=driver.find_element(By.XPATH,'//div[@class="ui-autocomplete-multiselect ui-state-default ui-widget"]')
# language.click()
# time.sleep(2)
# dropdownlist=driver.find_elements(By.CSS_SELECTOR,'li.ng-scope')
# selectvalues(dropdownlist,'English')
# selectvalues(dropdownlist,'Arabic')
# selectvalues(dropdownlist,'Catalan')
#making a list and sending multiple values and single values
# def selectvalues(ele_list,value):
#     for ele in dropdownlist:
#         print(ele.text)
#         for k in range(len(value)):
#             if ele.text==value[k]:
#                 ele.click()
#                 break
#
# language=driver.find_element(By.XPATH,'//div[@class="ui-autocomplete-multiselect ui-state-default ui-widget"]')
# language.click()
# time.sleep(2)
# dropdownlist=driver.find_elements(By.CSS_SELECTOR,'li.ng-scope')
# valuelist=['Arabic','English','Hindi','Catalan']
# #valuelist=['English']
# selectvalues(dropdownlist,valuelist)
#To select all dropdown list
