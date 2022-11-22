from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I launch Chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome("webdriver/chromedriver.exe")

@when('I open orange HRM Homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")



@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    print(user, pwd)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.NAME, "username").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(pwd)

@when('Click on login button')
def step_impl(context):
    context.driver.find_element(By.TAG_NAME, "button").click()
    context.driver.implicitly_wait(10)

@then('User must successfully login to the Dashboard')
def step_impl(context):
    try:
        context.driver.implicitly_wait(10)
        text = context.driver.find_element(By.XPATH, "//span[text()='Cockpit']").text
    except:
        context.driver.close()
        assert False, "Test Failed"

    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"


