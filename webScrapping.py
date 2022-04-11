import time

from openpyxl import Workbook
from selenium import webdriver
import openpyxl
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


driver=webdriver.Chrome(executable_path="D:\drivers\chromedriver.exe")
driver.get('https://www.homechoice.co.za/home')
driver.maximize_window()
driver.implicitly_wait(5)
searchbox=driver.find_element(By.ID,'CC-headerWidget-Search')
searchbox.send_keys("beds")
clickbtn=driver.find_element(By.ID,'searchSubmit').click()
filterbtn=driver.find_element(By.XPATH,'//span[contains(text(),"HomeChoice")]')
filterbtn.click()
bedProducts=driver.find_elements(By.XPATH,'//h3[contains(@itemprop,"name")]')
print("beds present in current page",len(bedProducts))
mybeds=[]
myprice=[]
for bed in bedProducts:
    # print(bed.text)
    mybeds.append(bed.text)
print("=*"*50)
time.sleep(2)
bedPrices=driver.find_elements(By.XPATH,'//div[@itemprop="cash-price"]')
my_element_id = '//span[contains(@id,"CC-product-price-max")]'
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)
print("prices present in a current page",len(bedPrices))
bedPrices = WebDriverWait(driver,10,ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_all_elements_located((By.XPATH, my_element_id)))

for price in bedPrices:
    # print(price.text)
    myprice.append(price.text)

finallist=zip(mybeds,myprice)

# for data in list(finallist):
#     print(data)

print("part1 completed")
wb=Workbook()
wb["Sheet"].title="BEDS DATA"
sh1=wb.active
sh1.append(["name","price"])
for x in list(finallist):
    sh1.append(x)
wb.save("beddetail.xlsx")
print("part2 is completed")