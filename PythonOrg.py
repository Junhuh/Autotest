import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        #这样可以根据需要自动加载时间
        self.driver.implicitly_wait(30)
        self.base_url="http://www.python.org"
        self.verficationErrors=[]
        self.accept_next_alert=True
    def test_search(self):
        driver = self.driver
        driver.get(self.base_url+"/")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("selenium")
        elem.send_keys(Keys.RETURN)
        #判断title中是否有Welcome字段
        self.assertIn("Welcome", driver.title)
        driver.close()
    def test_download(self):
        driver = self.driver
        driver.get(self.base_url+"/")
        self.assertIn("Python", driver.title)
        link=driver.find_element_by_link_text("Downloads")
        link.click()
        time.sleep(3)
        driver.close()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verficationErrors)
if __name__ == "__main__":
    unittest.main()