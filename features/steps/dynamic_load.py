from behave import *
from selenium import webdriver
from behave import given
import time

from behave_webdriver.steps import *


from IPython import embed

@given('I reach the internet page')
def step_impl(context):
   context.browser.get("https://the-internet.herokuapp.com")


@given('I select dynamic loading')
def select_dym_load(context):
    context.browser.find_element_by_xpath("//*[@id='content']/ul/li[14]/a").click()

@given('I click example two')
def select_exam_two(context):
    context.browser.find_element_by_xpath("//*[@id='content']/div/a[2]").click()





