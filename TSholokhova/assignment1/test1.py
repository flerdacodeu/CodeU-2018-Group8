import unittest
from time import time
from task1 import is_anagram, is_anagram_linear


class TestAnagrams(unittest.TestCase):
    def test_words_basic(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("listen", "silent", case_sensitive=False))

        self.assertFalse(is_anagram("abc", "ab"))
        self.assertFalse(is_anagram("abc", "ab", case_sensitive=False))

        self.assertFalse(is_anagram("Triangle", "integral"))
        self.assertTrue(is_anagram("Triangle", "integral", case_sensitive=False))

        self.assertTrue(is_anagram("", ""))
        self.assertTrue(is_anagram("", "", case_sensitive=False))

    def test_words_advance(self):
        self.assertTrue(is_anagram("listen" * 100000, "silent" * 100000))
        self.assertTrue(is_anagram("listen" * 100000, "silent" * 100000, case_sensitive=False))

        self.assertFalse(is_anagram("Triangle" * 100000, "integral" * 100000))
        self.assertTrue(is_anagram("Triangle" * 100000, "integral" * 100000, case_sensitive=False))

    def test_sentences(self):
        self.assertFalse(is_anagram("Hello, how are you?", "?uoy era woh, olleH", punctuation="none"))
        self.assertTrue(is_anagram("Hello, how are you?", "?uoy era woh, olleH", punctuation="ignore"))
        self.assertTrue(is_anagram("Hello, how are you?", "?uoy era woh, olleH", punctuation="spaces"))


        self.assertTrue(is_anagram("hello!", "he!llo", punctuation="none"))
        self.assertTrue(is_anagram("hello!", "he!llo", punctuation="ignore"))
        self.assertTrue(is_anagram("hello!", "he.llo", punctuation="ignore"))
        self.assertFalse(is_anagram("hello!", "he!llo", punctuation="spaces"))

class TestEfficient():
    def test_time1(self):
        """
        Execute two is_anagram functions many times with short strings parameters to compare working time.
        """
        s = 'bcdefghijkalmnopqrstuvwxyz'
        t0 = time()
        for i in range(50000):
            is_anagram(s, s[::-1])
        time_nlogn = time() - t0

        t0 = time()
        for i in range(50000):
            is_anagram_linear(s, s[::-1])
        time_linear = time() - t0
        print("\n Linear: {0:.2f} s. \n N log(N): {1:.2f} s.".format(time_linear, time_nlogn))

    def test_time2(self):
        """
        Execute two is_anagram functions once with long strings parameters to compare working time.
        """
        s = 'bcdefghijkalmnopqrstuvwxyz'
        t0 = time()
        is_anagram(s*500000, s[::-1]*500000)
        time_nlogn = time() - t0

        t0 = time()
        is_anagram_linear(s*500000, s[::-1]*500000)
        time_linear = time() - t0
        print("\n Linear: {0:.2f} s. \n N log(N): {1:.2f} s.".format(time_linear, time_nlogn))


if __name__ == '__main__':
    unittest.main()

