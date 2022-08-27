#dropdownlist,radiobutton everthing is coverd
#is selected css selector and select method practice
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
#driver=webdriver.Chrome('G:\driver\chromedriver_win32\chromedriver.exe')
driver=webdriver.Chrome()#my pc
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
#entering 1st and second name
driver.find_element(By.XPATH,'//input[@ng-model="FirstName"]').send_keys("pavithrabalan")
driver.find_element(By.XPATH,'//input[@ng-model="LastName"]').send_keys("sethu")
time.sleep(2)
#adress
tb2=driver.find_element(By.XPATH,'//*[@ng-model="Adress"]')
print("--adress--")
print("displayed--->",tb2.is_displayed())
print("enabled--->",tb2.is_enabled())
tb2.send_keys("chrompet,chennai")
#mail and mobile number
driver.find_element(By.XPATH,'//*[@ng-model="EmailAdress"]').send_keys("abc@gdsgmail.com")
driver.find_element(By.XPATH,'//input[@ng-model="Phone"]').send_keys("9874563215")
time.sleep(2)
#gender radio button selection
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
#scroll down
scroll_down=driver.find_element(By.XPATH,'//label[text()="Gender*"]')
driver.execute_script("arguments[0].scrollIntoView();",scroll_down)
#hobbies
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
#language is not a select type so i am using here css_selector and function method
#language=driver.find_element(By.ID,'id="msdd"')
def selectvalues(ele_list,value):
    for ele in dropdownlist:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break
language=driver.find_element(By.XPATH,'//div[@class="ui-autocomplete-multiselect ui-state-default ui-widget"]')
language.click()
time.sleep(2)
dropdownlist=driver.find_elements(By.CSS_SELECTOR,'li.ng-scope')
selectvalues(dropdownlist,'English')
selectvalues(dropdownlist,'Arabic')
selectvalues(dropdownlist,'Catalan')
#skill
skill=driver.find_element(By.XPATH,'//select[@id="Skills"]')#identify the web elements
skills=Select(skill)#assign with variable with select method
opskil=skills.options#select all options to print index or value
skills.select_by_index(2)#select method
skills.select_by_value("Android")
time.sleep(2)
skills.select_by_visible_text('AutoCAD')
time.sleep(2)
lenskil=len(opskil)
print("total skills",lenskil)
print("---skills list---")
for i in range(0,77):
    print(opskil[i].text)
print("--index 35 to 45 skills--")
for k in range(35,45):
    print(opskil[k].text)
print("skills done")
print("country")
country=driver.find_element(By.XPATH,'//select[@id="country"]')
print("country is selected",country.is_selected())
countries=Select(country)
countries.select_by_value("India")
time.sleep(2)
countries.select_by_index(10)
time.sleep(2)
countries.select_by_visible_text('Netherlands')
print("country is selected",country.is_selected())
opcountry=countries.options
countyrlen=len(opcountry)
print("total number of countries:",countyrlen)
print('list of country')
for world in range(0,11):#variable world stores index
    print(opcountry[world].text)
print("==years==")
year=driver.find_element(By.XPATH,'//select[@id="yearbox"]')
years=Select(year)
years.select_by_index(3)
time.sleep(2)
years.select_by_visible_text("1997")
time.sleep(2)
years.select_by_value("1973")
opyear=years.options
lenyear=len(opyear)
print("total options in year",lenyear)
for me in range(101):
    print(opyear[me].text)
print('==between year==')
for a in range(12,30):
    print(opyear[a].text)

print("==months==")
month=driver.find_element(By.XPATH,'//select[@ng-model="monthbox"]')
months=Select(month)
time.sleep(2)
months.select_by_index(5)
opmonth=months.options
monthlen=len(opmonth)
print(monthlen)
time.sleep(2)
for index in range(1,5):
    print(opmonth[index].text)
print("==done==")
print("==days==")
day=driver.find_element(By.XPATH,'//select[@id="daybox"]')
days=Select(day)
days.select_by_index(4)
time.sleep(2)
opdays=days.options
lendays=len(opdays)
print("total options in days\n",lendays)
print('--days list--')
for pavi in range(31):
    print(opdays[pavi].text)
print("===done===")
driver.find_element(By.XPATH,'//input[@id="firstpassword"]').send_keys("123456")
driver.find_element(By.XPATH,'//input[@id="secondpassword"]').send_keys("123456")
time.sleep(2)
#driver.find_element(By.XPATH,'//*[@id="submitbtn"]').click()
time.sleep(10)
driver.close()# its close the window