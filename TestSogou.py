#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import unittest
import time
import re
import HTMLTestRunner

class TestSogou(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome()
        self.browser.implicitly_wait(30)
        self.base_url="https://www.sogou.com"
        self.verficationErrors=[]
        self.accept_next_alert=True
    def test_search(self):
        browser=self.browser
        browser.get(self.base_url+'/')
        browser.maximize_window()
        keyworld=browser.find_element_by_name("query")
        keyworld.send_keys("Selenium Python")
        browser.find_element_by_id("stb").click()
        time.sleep(3)
        browser.close()
    def test_weixin(self):
        browser=self.browser
        browser.get(self.base_url+'/')
        browser.maximize_window()
        browser.find_element_by_link_text("微信").click()
        time.sleep(2)
        browser.close()
    def test_config(self):
        browser=self.browser
        browser.get(self.base_url+'/')
        browser.maximize_window()
        browser.find_element_by_class_name("s_usersetting").click()
        time.sleep(2)
        browser.close()
    def tearDown(self):
        self.browser.quit()
        self.assertEqual([],self.verficationErrors)

if __name__=="__main__":
    unittest.main()