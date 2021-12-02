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
driver.get("https://www.myntra.com/")

driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div[2]/div[3]/input").send_keys("Maybelline")

time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div[2]/div[3]/a/span").click()
time.sleep(2)
driver.get("https://www.myntra.com/foundation-and-primer/maybelline/maybelline-fit-me-set-of-concealer--matte-foundation/15060308/buy")
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/main/div[2]/div[2]/div[3]/div/div[1]").click()

driver.find_element_by_xpath("/html/body/div[2]/div/div/div/main/div[2]/div[2]/div[3]/div/a/span[2]").click()
print("Program successfull")
driver.close()