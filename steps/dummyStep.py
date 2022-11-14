from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I open the browser')
def openApp(context):
      print('******************************** Book details entered ******************************** ')
      driver = webdriver.Chrome();
      driver.maximize_window();
      driver.get("https://www.google.com");
      driver.find_element(By.XPATH, "//div[text()='Reject all']").click();
      driver.find_element(By.XPATH, "// input[ @ title = 'Search']").send_keys("is it that time of the year?");
      driver.quit();
@then('login to the application')
def quitApp(context):
      print('********************************  Verify book name ******************************** ')
