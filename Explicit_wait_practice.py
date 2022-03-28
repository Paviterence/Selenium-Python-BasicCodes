# title_is
# title_contains
# presence_of_element_located
# visibility_of_element_located
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
driver=webdriver.Chrome("D:\drivers\chromedriver.exe")#my pc
#title1=WebDriverWait(driver,20).until(Ec.url_to_be('http://demo.automationtesting.in/Index.html'))
driver.get('http://demo.automationtesting.in/Index.html')
# driver.maximize_window()
tb1=WebDriverWait(driver,5).until(Ec.presence_of_element_located((By.ID,"email")))
tb1.send_keys("pavithrabalan")
button1=WebDriverWait(driver,5).until(Ec.visibility_of_element_located((By.ID,"enterimg")))
button1.click()
fname=WebDriverWait(driver,5).until(Ec.text_to_be_present_in_element((By.XPATH,'//input[@ng-model="FirstName"]')))
fname.send_keys("pavithrabalan")