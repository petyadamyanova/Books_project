import unittest
from book import *

class Test(unittest.TestCase):
    def test_if_published_year_is_correct(self):
        self.assertFalse(ckeck_if_published_year_is_correct(1400))
        self.assertFalse(ckeck_if_published_year_is_correct(2200))
        self.assertTrue(ckeck_if_published_year_is_correct(1503))
        self.assertTrue(ckeck_if_published_year_is_correct(2020))
    def test_ckeck_if_series_are_correct(self):
        self.assertFalse(ckeck_if_series_are_correct("jdcnkc"))
        self.assertFalse(ckeck_if_series_are_correct("334"))
        self.assertTrue(ckeck_if_series_are_correct("True"))
        self.assertTrue(ckeck_if_series_are_correct("False"))
        
        
        
     



