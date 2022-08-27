from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
# s=Service(executable_path='D:\drivers\chromedriver.exe')
driver=webdriver.Chrome()
driver.get("http://demo.guru99.com/test/write-xpath-table.html")
driver.maximize_window()

tableRow = driver.find_elements(By.TAG_NAME,"tr")
lengthVal = len(tableRow)
print("table Row-->\n",lengthVal)
#/2 rows
print("number of data available below here")
tabledatas = driver.find_elements(By.TAG_NAME,"td")
lengthdata = len(tabledatas)
print("table data-->",lengthdata)
# Table data tags 4
print("-------------****------------")
print("data available in the table below here")
for index in tabledatas:
    res = index.text
    print("res-->\n",res)
print("----------****----------------")


# Nested for loop  // C lang
for i in tableRow:
    # 0, 1
    tdats = i.find_elements(By.TAG_NAME, "td")
    print("tdats-->\n",i.text)
    for j in tdats:
        print(j.text)

print("----------****----------------")
#
tablecount = driver.find_elements(By.TAG_NAME,"table")
length = len(tablecount)
print("length-->\n",length)
# 1
print("-------------------------------------------")
firstableData = tablecount[0].find_elements(By.TAG_NAME,"td")
for i in firstableData:
    print(i.text)

# <table>
    # <tr>
        # <td> ram </td>
    # </tr>
    # <tr>
    # <td> raja </td>
# </tr>
# <tr>
# <td> abc </td>
# </tr>
# </table>
print("----------------")
# <table> Table
#  <tr> Table Row
# <td>  Table Data
# <th>  Table header

# Script - Tester
# query - back end Dev
# Code  - Front end dev

# Dom - Document object model
#  Eclipse
#  Liclipse
#  Intellji
#  RIDE
