import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
user_input=input("please enter what you want from youtube\n:")
driver=webdriver.Chrome(executable_path='D:\drivers\chromedriver.exe')
driver.fullscreen_window()
driver.get("https://www.youtube.com/")
driver.fullscreen_window()
print((driver.title))
print(driver.current_url)
wait=WebDriverWait(driver,20)
searchbox=wait.until(ec.visibility_of_element_located((By.XPATH,'//input[@id="search"and@name="search_query"and @tabindex="0"and@type="text"]')))
searchbox.send_keys(user_input)
# button=wait.until(ec.element_to_be_clickable((By.XPATH,'//button[@id="search-icon-legacy"and @class="style-scope ytd-searchbox"and @aria-label="Search"')))
# button.click()
time.sleep(2)
driver.find_element_by_xpath('//button[@id="search-icon-legacy"and @class="style-scope ytd-searchbox"and @aria-label="Search"]').click()
time.sleep(2)
current_song=driver.find_element(By.XPATH,'(//a[@id="video-title"])[1]')
current_song.click()
time.sleep(5)
# fullscreen=wait.until(ec.element_to_be_clickable((By.XPATH,'(//*[@class="ytp-fullscreen-button ytp-button"])[1]')))
# fullscreen.click()
time.sleep(50)
driver.back()
time.sleep(2)
ak2=driver.find_element(By.XPATH,'(//a[@id="video-title"])[2]')
ak2.click()
time.sleep(50)
driver.back()
ak3=driver.find_element(By.XPATH,'(//a[@id="video-title"])[3]')
ak3.click()
time.sleep(50)
driver.quit()