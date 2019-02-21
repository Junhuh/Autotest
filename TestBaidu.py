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
class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome()
        self.browser.implicitly_wait(30)
        self.base_url="http://www.baidu.com"
        self.verficationErrors=[]
        self.accept_next_alert=True
    def test_search(self):
        browser = self.browser
        browser.get(self.base_url+'/')
        browser.find_element_by_id("kw").clear()
        browser.find_element_by_id("kw").send_keys("自动化测试")
        browser.find_element_by_id("su").click()
        time.sleep(2)
        browser.find_element_by_id("su").submit()
        time.sleep(3)
        title=browser.title
        print ("title is %s"%title)
        time.sleep(5)
        browser.close()
    def test_link(self):
        browser=self.browser
        browser.get(self.base_url+'/')
        browser.find_element_by_link_text("贴吧").click()
        time.sleep(5)
        browser.close()
    def tearDown(self):
        self.browser.quit()
        self.assertEqual([],self.verficationErrors)
if __name__=="__main__":
    unittest.main()