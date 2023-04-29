#coding=utf-8

from  selenium import webdriver
from selenium.webdriver.common .by import By
import unittest
from time import sleep




class testruner(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.url="http://www.baidu.com"
    def tearDown(self):
        self.driver.quit()


    def test_1(self):
        driver=self.driver
        driver.get(self.url)
        sleep(3)
        driver.find_element(By.ID,"kw").send_keys("中文")
        sleep(3)
        driver.find_element(By.ID,"su").click()
        sleep(3)
        self.assertEqual(driver.current_url,"http://www.baidu.com",msg="网址未发生移动")
    def test_2(self):
        driver = self.driver
        driver.get(self.url)
        sleep(3)
        driver.find_element_by_id("kw").send_keys("123456")
        sleep(3)
        driver.find_element_by_id("su").click()
        sleep(3)
        self.assertNotEqual(driver.current_url,"http://www.baidu.com",msg="网址未发生移动")




