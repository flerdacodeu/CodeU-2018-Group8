from collections import Counter
import unittest

def is_anagram(s1, s2, case_sensitive=True):
    """
    A method that checks whether two strings are anagrams of each other.
        - s1 - str, first input string.
        - s2 - str, second input string. 
        - case_sensitive - boolean, specifying whether checking for 
                           anagrams is case sensitive or not.
        Returns: boolean, True if s1 and s2 are anagrams of each other,
                 False otherwise.
    """
    if len(s1) != len(s2):
        return False
    if not case_sensitive:
        s1 = s1.lower()
        s2 = s2.lower()
    s1_counter = Counter(s1)
    s2_counter = Counter(s2)
    return s1_counter == s2_counter


class AnagramTest(unittest.TestCase):

    def test_case_sensitive1(self):
        self.assertTrue(is_anagram("Apple", "pAlpe"))

    def test_case_sensitive2(self):
        self.assertFalse(is_anagram("Apple", "palpe"))

    def test_case_empty(self):
        self.assertTrue(is_anagram("", ""))

    def test_case_insensitive1(self):
        self.assertTrue(is_anagram("Apple", "palpe", case_sensitive=False))

    def test_case_insensitive2(self):
        self.assertFalse(is_anagram("applt", "palpe", case_sensitive=False))


if __name__ == "__main__":
    unittest.main()