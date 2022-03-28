import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import service

#driver = webdriver.Chrome(executable_path="G:\driver\chromedriver_win32\chromedriver.exe") #my computer
driver=webdriver.Chrome("D:\drivers\chromedriver.exe")
driver.implicitly_wait(40)
driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH,'//a[@role="button"and@data-testid="open-registration-form-button"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//input[@name="firstname"and@aria-label="First name"]').send_keys('pavithran')
time.sleep(2)
driver.find_element(By.XPATH,'//input[@name="lastname"and@aria-label="Surname"]').send_keys('sethu')
time.sleep(2)
driver.find_element(By.XPATH,'//input[@aria-label="Mobile number or email address"]').send_keys('9784561524')
driver.find_element(By.XPATH,'//input[@id="password_step_input"and@type="password"]').send_keys('Passcode')
time.sleep(2)
print("--------days-------")
days_elements=driver.find_element(By.ID,"day")#assign the id
days=Select(days_elements)#selecting the all elements
#giving the values manually to the dropdownlist
days.select_by_visible_text("17")#text method
time.sleep(2)
days.select_by_index(2)#index method
time.sleep(2)
days.select_by_value("6")#value method
time.sleep(2)
days_elements.send_keys("25")#send my value to days dropdown box NORMAL METHOD
print("get attribute method the value sent to the dropbox:",days_elements.get_attribute('value')) #get my value from dropbox
time.sleep(2)
totaloptions=len(days.options)#to find total options available in days
print("Total options in day dropdownlist:",totaloptions)#31 options are there
opsd=days.options#to get all options
print("total options")#just for heading
for option in opsd:#for loop
    print("option text is-{}-option value is={}".format(option.text,option.get_attribute("value")))
print("--using range--")
for x in range(0,30):
    print(opsd[x].text)
print("--days after 20th\n--")
for x in opsd:
    y=x.get_attribute("value")
    z=int(y)
    if z>=20:
        print(x.text)

print("--days between 10 to 25\n--")
for x in opsd:
    y=x.get_attribute("value")
    z=int(y)
    if z>=10 and z<=25:
         print(x.text)

print('-----month-----')
#month

month_element=driver.find_element(By.ID,'month')
months=Select(month_element)
months.select_by_value("2")#feb
time.sleep(2)
months.select_by_index(4)
time.sleep(2)
months.select_by_visible_text("Aug")
month_length=len(months.options)
print("total months options are available in facebook\n:",month_length)
ops=months.options
for option in ops:
   print("option text is-{}-option value is={}".format(option.text, option.get_attribute("value")))
#using range printing text
print("--using range--")
for x in range(0,12):
    print(ops[x].text)

print("----last 3 months---\n")
for x in ops:
    y=(x.get_attribute('value'))
    z=int(y)
    if z>=10:
        print(x.text)
print("----between months:----\n")
for x in ops:
    y=(x.get_attribute('value'))
    z=int(y)
    if z>=2 and z<=10:
        print(x.text)
print("---1st 3 months\n---")
for x in ops:
    y=(x.get_attribute('value'))
    z=int(y)
    if z<=3:
        print(x.text)

print("-------year--------")
year_elements=driver.find_element(By.ID,"year")
years=Select(year_elements)
years.select_by_visible_text("1997")
time.sleep(3)
years.select_by_value("1996")
time.sleep(3)
years.select_by_index(1)#2021
totalyears=len(years.options)
print("total no of options in year:",totalyears)#118
opsy=years.options
for x in opsy:
   print("year is={} year value is={}".format(x.text,x.get_attribute("value")))
print("--using range--")
for x in range(0,30):
    print(opsy[x].text)
print("--years above 1997\n--")
for x in opsy:
    y=x.get_attribute("value")
    z=int(y)
    if z>=1997:
        print(x.text)
print("--years between 2000 to 1990\n--")
for x in opsy:
    y=x.get_attribute("value")
    z=int(y)
    if z<=2000 and z>=1990:
        print(x.text)

print(type(y))
print(type(z))


#gender selection
gender_f=driver.find_element(By.XPATH,'(//input[@type="radio"and@name="sex"])[1]').click()
status=driver.find_element(By.XPATH,'(//input[@type="radio"and@name="sex"])[1]').is_selected()
print(status)
time.sleep(3)
gender_m=driver.find_element(By.XPATH,'(//input[@type="radio"and@name="sex"])[2]').click()
status=driver.find_element(By.XPATH,'(//input[@type="radio"and@name="sex"])[2]').is_selected()
print(status)
time.sleep(3)
gender_c=driver.find_element(By.XPATH,'(//input[@type="radio"and@name="sex"])[3]').click()
status=driver.find_element(By.XPATH,'(//input[@type="radio"and@name="sex"])[3]').is_selected()
print(status)
custom=driver.find_element(By.XPATH,'//select[@aria-label="Select your pronoun"]')
custom_s=Select(custom)
custom_s.select_by_value("1")
time.sleep(2)
custom_s.select_by_value("2")
time.sleep(2)
customs=custom_s.options
for x in customs:
    print(x.text)
driver.find_element(By.XPATH,'//input[@name="custom_gender"]').send_keys("they")

driver.find_element(By.XPATH,'//button[text()="Sign Up"]').click()
time.sleep(5)
driver.close()
