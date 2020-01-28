"""
Program: test_camper_age_input.py
Author: Mohammad Noori
Last date modified: 01/27/2020
This tests the program for converts age in years to months.
"""
import unittest
from main import camper_age_input


class MyTestCase(unittest.TestCase):  # test class
    def test_multi(self):  # Function definition.
        # This tests the function convert_to_months in camper_age_input.py.
        self.assertEquals(camper_age_input.convert_to_months(5, 6), 30)  # Function definition.



if __name__ == '__main__':
    unittest.main()  # call the function.
