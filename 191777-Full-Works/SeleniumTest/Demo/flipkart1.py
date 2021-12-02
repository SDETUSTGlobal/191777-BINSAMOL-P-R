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
driver.get("https://www.flipkart.com/")

driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
driver.find_element_by_name("q").send_keys("Maybelline")
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()
time.sleep(2)

driver.get("https://www.flipkart.com/maybelline-new-york-fit-me-matte-poreless-liquid-foundation-with-pump-spf-22-230-natural-buff-30ml/p/itmfcbbffbb9b21c?pid=FNDGY5GNHNARFNKS&lid=LSTFNDGY5GNHNARFNKSUHBZFW&marketplace=FLIPKART&q=maybelline+foundation&store=g9b%2Fffi%2Fdzu%2Fgru&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_10_na_na_na&fm=SEARCH&iid=85ced993-692f-429d-a272-2d09d01e5902.FNDGY5GNHNARFNKS.SEARCH&ppt=sp&ppn=sp&ssid=ie8wmvrng00000001637751642827&qH=e4724021097c163c")
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button").click()


driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button").click()



driver.close()
print("successfully completed")