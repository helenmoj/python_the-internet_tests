from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By


#@given(u'I reach the internet page')

@step(u'I reach the internet page')
def step_impl(context):
    context.dynamic_load.navigate("https://the-internet.herokuapp.com")
    assert_equal(context.home_page.get_page_title(), "PyPI - the Python Package Index : Python Package Index")
