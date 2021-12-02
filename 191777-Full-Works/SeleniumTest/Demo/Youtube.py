import time

from selenium import webdriver
from selenium.webdriver import Keys

driver = webdriver.Chrome("E:\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.youtube.com/")
driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("Michael Jackson")
time.sleep(3)
#click on the Google search button
driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon").click()
time.sleep(3)
#close the browser
driver.close()
print("sample test case successfully completed")