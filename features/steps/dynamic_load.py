from behave import *
from selenium import webdriver
from behave import given
import time

from IPython import embed

from behave_webdriver.steps import *


#from IPython import embed
import IPython

@given('I reach the internet page')
def step_impl(context):
    context.browser.get("https://the-internet.herokuapp.com")


@given('I select dynamic loading')
def select_dym_load(context):
    context.browser.find_element_by_xpath("//*[@id='content']/ul/li[14]/a").click()


@given('I click example two')
def select_exam_two(context):
    context.browser.find_element_by_xpath("//*[@id='content']/div/a[2]").click()

@given('I see the text \'Example 2: Element rendered after the fact\' is displayed')
def text(context):
    status = context.browser.find_element_by_xpath("//*[@id='content']/div/h3").is_displayed()
    assert status is True

@given('I select the start button')
def start_button(context):
    context.browser.find_element_by_id('start').click()









