from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

print("test case started")
# open Google Chrome browser
driver = webdriver.Chrome("E://chromedriver_win32//chromedriver")
# maximize the window size
driver.maximize_window()
# delete the cookies
driver.delete_all_cookies()
driver.get("http://secure.smartbearsoftware.com/samples/testcomplete11/WebOrders/login.aspx");
driver.find_element_by_id("ctl00_MainContent_username").send_keys("Tester");
time.sleep(3)
driver.find_element_by_id("ctl00_MainContent_password").send_keys("test");
time.sleep(3)
driver.find_element_by_id("ctl00_MainContent_login_button").click();
driver.find_element_by_id("ctl00_MainContent_btnCheckAll").click();

driver.find_element_by_id("ctl00_MainContent_btnDelete").click();
driver.find_element_by_id("ctl00_MainContent_orderLInk").click();
driver.back();
driver.back();
driver.find_element_by_id("ctl00_MainContent_btnUncheckAll").click();
driver.find_element_by_id("ctl00_MainContent_orderGrid_ctl02_OrderSelector").click();
driver.find_element_by_id("ctl00_MainContent_btnUncheckAll").click();
driver.find_element_by_link_text("View all products").click();
driver.find_element_by_partial_link_text("Order").click();
driver.find_element_by_css_selector("#ctl00_MainContent_fmwOrder_txtQuantity").send_keys("1000");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_txtUnitPrice").send_keys("80");
driver.find_element_by_xpath(
    "/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]").click();

driver.find_element_by_name("ctl00$MainContent$fmwOrder$txtName").send_keys("Nick");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox2").send_keys("BakerStreet");

driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox3").send_keys("London");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox4").send_keys("UK");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox5").send_keys("009568");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_cardList_0").click();
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox6").send_keys("123456789012");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox1").send_keys("01/23");

driver.find_element_by_xpath(
    "/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]").click()
dropdown = Select(driver.find_element_by_id("ctl00_MainContent_fmwOrder_ddlProduct"));
dropdown.select_by_visible_text("FamilyAlbum");
driver.find_element_by_css_selector("#ctl00_MainContent_fmwOrder_txtQuantity").send_keys("1000");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_txtUnitPrice").send_keys("80");
driver.find_element_by_xpath(
    "/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]").click();


print("Run Successfully")
driver.close()