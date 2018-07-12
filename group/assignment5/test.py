import unittest
from code import get_alphabet

class TestDictionary(unittest.TestCase):
    def test_empty_dictionary(self):
        words = []
        self.assertListEqual(get_alphabet(words), [])

    def test_empty_words(self):
        words = ['', '']
        self.assertListEqual(get_alphabet(words), [])

    def test_1_word(self):
        words = ['abc']
        self.assertTrue(get_alphabet(words) in [['a', 'b', 'c'],
                                                ['a', 'c', 'b'],
                                                ['b', 'a', 'c'],
                                                ['b', 'c', 'a'],
                                                ['c', 'a', 'b'],
                                                ['c', 'b', 'a']])

    def test_1_character(self):
        words = ['a', 'aaa', 'aaaa']
        self.assertListEqual(get_alphabet(words), ['a'])

    def test_3_words(self):
        words = ['at', 'bat', 'tab']
        self.assertListEqual(get_alphabet(words), ['a', 'b', 't'])

    def test_prefix_words(self):
        words = ['ab', 'ac', 'ad']
        self.assertTrue(get_alphabet(words) in [['a', 'b', 'c', 'd'],
                                                ['b', 'a', 'c', 'd'],
                                                ['b', 'c', 'a', 'd'],
                                                ['b', 'c', 'd', 'a']])
    def test_no_consistent_alphabet(self):
        words = ['a', 'b', 'c', 'a']
        self.assertEqual(get_alphabet(words), -1)

if __name__ == '__main__':
    unittest.main()