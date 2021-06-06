import unittest
from book import *
from user import *

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
    def test_ckeck_if_password_is_correct(self):
        self.assertFalse(check_if_password_is_correct("abnbI5"))
        self.assertFalse(check_if_password_is_correct("78998998"))
        self.assertFalse(check_if_password_is_correct("abnbik0"))
        self.assertTrue(check_if_password_is_correct("Abcdef123"))
        self.assertTrue(check_if_password_is_correct("A1bdft67"))
        self.assertTrue(check_if_password_is_correct("Petyadam1234"))
    def test_check_if_sex_is_correct(self):
        self.assertFalse(check_if_sex_is_correct("abc"))
        self.assertFalse(check_if_sex_is_correct("0909"))
        self.assertFalse(check_if_sex_is_correct("a"))
        self.assertTrue(check_if_sex_is_correct("male"))
        self.assertTrue(check_if_sex_is_correct("female"))
        self.assertTrue(check_if_sex_is_correct("none"))
    def test_check_if_birthday_is_correct(self):
        self.assertFalse(check_if_birthday_is_correct(34.02.2000))
        self.assertFalse(check_if_birthday_is_correct(04.13.2000))
        self.assertFalse(check_if_birthday_is_correct(07.09.20))
        self.assertFalse(check_if_birthday_is_correct(07.09.2030))
        self.assertFalse(check_if_birthday_is_correct(07.09.0345))
        self.assertTrue(check_if_birthday_is_correct(09.02.2000))
        self.assertTrue(check_if_birthday_is_correct(09.02.2020))
        self.assertTrue(check_if_birthday_is_correct(10.10.1999))
    
        
        
        
     



