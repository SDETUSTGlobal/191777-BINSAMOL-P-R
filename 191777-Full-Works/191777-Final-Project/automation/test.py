from selenium import webdriver
import time

print("test case started")
# open Google Chrome browser
driver = webdriver.Chrome("E:\Pycharm\chromedriver.exe")
# maximize the window size
driver.maximize_window()
# delete the cookies
driver.delete_all_cookies()
# navigate to the url
driver.get("http://127.0.0.1:5000/")
time.sleep(2)
# identify the user name text box and enter the value
driver.find_element_by_id("fname").send_keys("Binsa")
time.sleep(2)
driver.find_element_by_id("uid").send_keys("191777")
time.sleep(1)
driver.find_element_by_id("coname").send_keys("Ust Global")
time.sleep(2)
driver.find_element_by_id("coemail").send_keys("191777@ust-global.com")
time.sleep(2)
# Click on submit button
driver.find_element_by_xpath("/html/body/form/div/button").click()
time.sleep(5)

# close the browser
driver.close()
print("Ust login has been successfully completed")