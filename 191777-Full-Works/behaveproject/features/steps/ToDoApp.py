import time

from behave import*
from selenium import webdriver
@given('I go to Advance boy to add item')
def launchbrowser(context):
   context.driver=webdriver.Chrome(executable_path="E:/chromedriver_win32/chromedriver")
   context.driver.get("https://lambdatest.github.io/sample-todo-app/")

@then('I Click on first checkbox and second checkbox')
def clickcheckbox(context):
    context.driver.find_element_by_name('li1').click()
    context.driver.find_element_by_name('li2').click()

@when('I enter item to add')
def enteritem(context):
    context.driver.find_element_by_id('sampletodotext').send_keys("Yey, Let's add it to list")

@when('I click add button')
def clickadd(context):
    context.driver.find_element_by_id('addbutton').click()


@then('I should verify the added item')
def verify(context):
    added_item = context.driver.find_element_by_xpath("//span[@class='done-false']").text

    time.sleep(2)

    if added_item in "Yey, Let's add it to list":
        return True
    else:
        return False