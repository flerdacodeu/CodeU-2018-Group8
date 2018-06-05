import unittest
from question1 import anagram_finder

class AnagramTesting(unittest.TestCase):
    """
    Unit testing for Anagram Finder
    """
    def test_given_test_cases(self):
        """
        Tests the given test cases for this assignment.
        """
        self.assertTrue(anagram_finder("listen", "silent"))
        self.assertTrue(anagram_finder("triangle", "integral"))
        self.assertFalse(anagram_finder("apple", "pabble"))

    def test_case_sensitivity(self):
        """
        Tests case sensitive argument of anagram_finder.
        """
        self.assertFalse(anagram_finder("ABC", "abc", True))
        self.assertTrue(anagram_finder("ABC", "abc", False))

if __name__ == '__main__':
    unittest.main()
