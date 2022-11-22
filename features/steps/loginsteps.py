from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I launch Chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome("webdriver/chromedriver.exe")

@when('I open orange HRM Homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()


@when('Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.NAME, "username").send_keys(user)
    context.driver.find_element(By.NAME, "password").send_keys(pwd)

@when('Click on login button')
def step_impl(context):
    context.driver.find_element(By.TAG_NAME, "button").click()

@then(u'User must successfully login to the Dashboard page')
def step_impl(context):
    text = context.driver.find_element(By.XPATH, "//span[contains(text(),'Dashboard']").text
    assert text == "Dashboard"
    context.driver.close()

