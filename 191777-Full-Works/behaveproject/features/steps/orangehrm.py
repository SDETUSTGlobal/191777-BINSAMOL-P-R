from behave import *
from selenium import webdriver

@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path="E:\\chromedriver_win32\\chromedriver.exe")



@when('open orange hrm homepage')
def openHomePage(context):

    context.driver.get("https://opensource-demo.orangehrmlive.com/")



@then('verify that logo present on page')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/img").is_displayed()
    assert status is True



@then('close browser')
def closeBrowser(context):
    context.driver.close()


