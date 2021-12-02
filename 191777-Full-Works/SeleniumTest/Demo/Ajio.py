from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("test case started")
# open Google Chrome browser
driver = webdriver.Chrome("E://chromedriver_win32//chromedriver")
# maximize the window size
driver.maximize_window()
# delete the cookies
driver.delete_all_cookies()
# navigate to the url
driver.get("https://www.ajio.com/")

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/header/div[3]/div[2]/form/div/div/input").send_keys("Maybelline")
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/header/div[3]/div[2]/form/div/button/span").click()
time.sleep(2)

driver.get("https://www.ajio.com/maybelline-the-blushed-nudes-eyeshadow-palette/p/4912991540_theblushednudes")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[3]/div/div[7]/div[1]/div[1]/div/span[2]").click()


driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[3]/div/div[7]/div[1]/div[1]/a/div/span[2]").click()



driver.close()
print("successfully completed")