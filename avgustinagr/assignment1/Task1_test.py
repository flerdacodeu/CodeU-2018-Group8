import unittest
from Task1 import*
class test_task1(unittest.TestCase):
    """ Unit tests for Task1 """
    def test_sent_anagrams(self):
        self.assertEqual(sent_anagrams("ellHo world","ldwor Hello",True), True)
        self.assertEqual(sent_anagrams("ellHo !world", "ldwor! Hello", True), True)
        self.assertEqual(sent_anagrams("ellHo !world", "ldwor! Helll", True), False)
        self.assertEqual(sent_anagrams("HELLO","hello", False), True)

    def test_words_anagrams(self):
        self.assertTrue(words_anagrams("Hello","Ehllo",False))
        self.assertFalse(words_anagrams("Hello","Ellho",True))
        self.assertTrue(words_anagrams("Hello","Ellho",False))
