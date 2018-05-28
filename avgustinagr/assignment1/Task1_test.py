import unittest
from Task1 import*
class test_task1(unittest.TestCase):
    """ Unit tests for Task1 """
    def test_sent_anagrams(self):
        self.assertEqual(sent_anagrams("ellHo world","ldwor Hello",1), True)
        self.assertEqual(sent_anagrams("ellHo !world", "ldwor! Hello", 1), True)
        self.assertEqual(sent_anagrams("ellHo !world", "ldwor! Helll", 1), False)
        self.assertEqual(sent_anagrams("HELLO","hello", 0), True)

    def test_words_anagrams(self):
        self.assertTrue(words_anagrams("Hello","Ehllo",0))
        self.assertFalse(words_anagrams("Hello","Ellho",1))
        self.assertTrue(words_anagrams("Hello","Ellho",0))
