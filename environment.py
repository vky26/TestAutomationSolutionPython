from selenium import webdriver
from behave import *
import allure
from allure import attachment_type


def before_feature(context,feature):
	print('********** before_feature ********** ')
	context.browser = webdriver.Chrome();


def after_feature(context,feature):
	print('**********   after_feature ********** ')
	context.browser.quit()

def after_step(context,feature):
	print('**********   after_step ********** ')
	allure.attach(context.browser.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)

