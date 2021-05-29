import unittest
from book import *

class Test(unittest.TestCase):
    def test_if_published_year_is_correct(self):
        self.assertFalse(ckeck_if_published_year_is_correct(1400))
        self.assertFalse(ckeck_if_published_year_is_correct(2200))
        self.assertTrue(ckeck_if_published_year_is_correct(1503))
        self.assertTrue(ckeck_if_published_year_is_correct(2021))
    def test_ckeck_if_series_are_correct(self):
        self.assertFalse(ckeck_if_series_are_correct("jdcnkc"))
        self.assertFalse(ckeck_if_series_are_correct("334"))
        self.assertTrue(ckeck_if_series_are_correct("True"))
        self.assertTrue(ckeck_if_series_are_correct("False"))


def discover_and_run(start_dir: str = '.', pattern: str = 'test*.py'):
    """Discover and run tests cases, returning the result."""
    tests = unittest.defaultTestLoader(start_dir, pattern=pattern)
    # We'll use the standard text runner which prints to stdout
    runner = unittest.TextTestRunner()
    result = runner.run(tests) # Returns a TestResult
    print(result.errors, result.failures) # And more useful properties
    return result

discover_and_run('.', 'test_book*.py')
        
        
        
     



