import os
import pathlib
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

def file_url(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# Set up the WebDriver
driver = webdriver.Chrome()  # Make sure chromedriver is in your PATH or provide the executable_path

class WebpageTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_title(self):
        self.driver.get(file_url("counter.html"))
        self.assertEqual(self.driver.title, "Counter")

    def test_increase(self):
        self.driver.get(file_url("counter.html"))
        increase = self.driver.find_element(By.ID, "increase")
        increase.click()
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "1")

    def test_decrease(self):
        self.driver.get(file_url("counter.html"))
        decrease = self.driver.find_element(By.ID, "decrease")
        decrease.click()
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "-1")

    def test_multiple_increase(self):
        self.driver.get(file_url("counter.html"))
        increase = self.driver.find_element(By.ID, "increase")
        for _ in range(3):
            increase.click()
        self.assertEqual(self.driver.find_element(By.TAG_NAME, "h1").text, "3")

if __name__ == "__main__":
    unittest.main()
