from behave import *
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


@given(u'User is on Home Page')
def step_imp(context):
    context.driver=Chrome()
    context.driver.get('https://education.softtechverse.com/')
    context.driver.maximize_window()
@when(u'User click on login button')
def step_imp(context):
    context.driver.get('https://education.softtechverse.com/authentication/index')

@when(u'User enters Username')
def step_imp(context):    
    context.driver.find_element(By.NAME, "email").send_keys("abcd")
    
@when(u'User enter Password')
def step_imp(context):
    context.driver.find_element(By.NAME,"password").send_keys("12345678")
    
@when(u'User click on Login button')
def step_imp(context):
    context.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    
@then(u'User should be registered successfully')
def step_imp(context):
    print("Registered Successfully")

    
    
