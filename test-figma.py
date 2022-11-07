# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from percy import percy_snapshot

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.blazedemo.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_demo(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1536,713 | ]]
        driver.get("https://findyourfreesamples.com/?cid=pbiqj&test=1&exp=FYFS-v2-FE-QA&mobile=9199823744&fname=jake&lname=luis")
       # browser.get('http://localhost:8000')
       # browser.implicitly_wait(10)
      #  new_todo_input = browser.find_element_by_class_name('new-todo')
       # percy_snapshot(browser, 'Empty Todo State')
        #percy_snapshot(driver, 'snapshot1');
        percy_snapshot(driver, 'snapshot2');
        percy_snapshot(
        driver=driver, 
        name='home page',
        widths=[768, 992, 1200, 414],
        percy_css="iframe { display: none; }"
        );
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
