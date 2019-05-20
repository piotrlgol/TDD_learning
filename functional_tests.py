from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_start_a_list_and_retrive(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test!")
        # User sees a field to enter item

        # types item

        # Item appears 

        # and new empty field. Adds another item

        # Two items

        # Special URL

        # Special URL works

if __name__ == '__main__':
    unittest.main()
