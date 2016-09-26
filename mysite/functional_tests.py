# My computer history web site as an example

# Boiler Plate


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        if os.name=='nt':
            self.browser = webdriver.Chrome()
        else:
            self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    #####################
    # END OF BOILER PLATE
    #####################

    def test_home_page(self):
        """
        
        This web site is an example of my understanding of the cluster class
        web site project.  It is a travelogue of the history of computers.
        
        The first thing you see is the home page which shows my homebrew
        computer and a heading, "The History of Computing" 
        
        """

        self.browser.get('http://localhost:8000/index.html')
        m=self.browser.find_element_by_tag_name('img')
        self.assertIn('homebrew.png',m.get_attribute('src'))
        h=self.browser.find_element_by_css_selector('h1')
        self.assertIn("The History of Computing",h.text)

if __name__=="__main__":
	unittest.main(warnings="ignore")
