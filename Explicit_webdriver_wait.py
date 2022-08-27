import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
driver=webdriver.Chrome()#my pc
driver.get('https://app.hubspot.com/login')
driver.set_page_load_timeout(30)#explict old method
print(driver.title)
wait=WebDriverWait(driver,10)
# wait.until(Ec.title_is('HubSpot Login'))#while loading sometimes eaxample checking browser it gives browser name as checking browser
wait.until(Ec.title_contains("HubSpot"))#so get the exact tittle we use this command
login_btn_check=driver.find_element(By.ID,'loginBtn')
print(login_btn_check.is_enabled())
usn=wait.until(Ec.presence_of_element_located((By.ID,'username')))
usn.send_keys("abcde@ymail.com")
pss=wait.until(Ec.presence_of_element_located((By.ID,'password')))
pss.send_keys("adahfdesr")
login_btn=wait.until(Ec.element_to_be_clickable((By.ID,'loginBtn')))
login_btn.click()
#time.sleep(5)
# driver.find_element(By.XPATH,'//*[text()="Sign up"]').click()
signup_button=WebDriverWait(driver,20).until(Ec.element_to_be_clickable((By.XPATH,'//*[text()="Sign up"]')))
signup_button.click()
time.sleep(5)
#website 2
#for alert in here we don't need to switch to alert while using the explict wait
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
print(driver.title)
sign_btn=wait.until(Ec.element_to_be_clickable((By.NAME,'proceed')))
sign_btn.click()
alert=wait.until(Ec.alert_is_present())#its automatically switch to alert
print("alert text is--->",alert.text)
alert.accept()
time.sleep(5)
#website 3
driver.get('http://demo.automationtesting.in/Index.html')
print(driver.title)
driver.maximize_window()
tb1=wait.until(Ec.presence_of_element_located((By.ID,"email")))#check the element in the dome
tb1.send_keys("pavithrabalan")
button1=wait.until(Ec.visibility_of_element_located((By.ID,"enterimg")))#check the element is present in ui or nott
button1.click()
driver.find_element(By.XPATH,'//input[@type="radio"and@ng-model="radiovalue"and@value="Male"]').click()
wait.until(Ec.element_located_to_be_selected((By.XPATH,'//input[@type="radio"and@ng-model="radiovalue"and@value="Male"]')))
time.sleep(5)
driver.close()