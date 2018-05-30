import unittest
from

class AnagramTesting(unittest.TestCase):
    """
    Unit testing for Anagram Finder
    """
    def given_test_cases(self):
        """
        Tests the given test cases for this assignment.
        """
        self.assertTrue(anagram_finder("listen", "silent"))
        self.assertTrue(anagram_finder("triangle", "integral"))
        self.assertFalse(anagram_finder("apple", "pabble"))


if __name__ == '__main__':
    unittest.main()
