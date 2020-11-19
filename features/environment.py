from selenium import webdriver
from browser import Browser
import behave_webdriver


def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.implicitly_wait(2)


def after_all(context):
    #context.browser.close()
    context.behave_driver.quit()

