from selenium.webdriver.common .by import By
import unittest
from time import sleep
from selenium import  webdriver
import  unittestreport

class MyTestCase(unittest.TestCase):
    def  setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = "http://www.jihujiasuqi.com/"
    def  tearDown(self) -> None:
        sleep(3)
        self.driver.close()
    def test_something(self):
        driver= self.driver
        driver.maximize_window()
        driver.get(self.url)
        sleep(3)
        driver.implicitly_wait(3)
        go_to_login_button = self.driver.find_elemen(By.CSS_SELECTOR,'a[class="action"]')
        go_to_login_button.click()

        self.assertEqual(driver.current_url,"http://www.jihujiasuqi.com/" ,msg="页面成功跳转")  # add assertion here






