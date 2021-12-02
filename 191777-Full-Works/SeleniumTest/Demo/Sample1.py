import time

from selenium import webdriver
from selenium.webdriver import Keys

driver = webdriver.Chrome("E:\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("java")
time.sleep(3)
#click on the Google search button
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(3)
#close the browser
driver.close()
print("sample test case successfully completed")