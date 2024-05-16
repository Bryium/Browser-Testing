import os
import pathlib
import unittest



from selenium import webdriver

def file_url(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()



driver = webdriver.Chrome()


class WebpageTests(unittest.TestCase):
    
    def test_title(self):
        driver.get(file_url("counter.html"))
        self.assertEqual(driver.title, "Counter")