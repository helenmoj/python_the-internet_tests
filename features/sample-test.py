import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SampleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # "/home/helen/anaconda3/lib/python3.7/site-packages/selenium/webdriver/common/service.py"

    def pypi_test(self):
        self.driver.get("https://the-internet.herokuapp.com")
        self.driver.find_element(By.ID, "term").send_keys("Selenium")
        self.driver.find_element(By.ID, "submit").click()

    def tearDown(self):
        self.driver.quit()
