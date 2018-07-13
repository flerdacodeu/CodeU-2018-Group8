# Python 3
import unittest
import sys
from nltk.corpus import wordnet
from word_search import *


class MySimpleDictionary(Dictionary):
    """
    A dictionary that assumes storage of only few words. 
    It is used for testing and 'is_prefix' is not optimized.
    """
    def __init__(self, words):
        self.words = set(words)

    def is_word(self, _str):
        """
        Returns whether the given string is a valid word. Not case sensitive
        :param _str: [string]
        :return: [bool] True/False
        """
        return True if _str in self.words else False

    def is_prefix(self, _str):
        """
        Returns whether the given string is a prefix of at least one word in the dictionary.
        If _str is empty string, returns False. Not case sensitive.
        :param _str: [string]
        :return: [bool] True/False
        """
        for word in self.words:
            if word.startswith(_str):
                return True
        return False


class EnglishDictionary(Dictionary):
    """
    A wrapper of the library nltk.corpus
    """

    def is_word(self, _str):
        """
        Returns whether the given string is a valid word. Not case sensitive
        :param _str: [string]
        :return: [bool] True/False
        """
        return True if wordnet.synsets(_str) else False

    def is_prefix(self, _str):
        """
        Returns whether the given string is a prefix of at least one word in the dictionary.
        If _str is empty string, returns False. Not case sensitive
        :param _str: [string]
        :return: [bool] True/False
        """
        return True if len(wordnet.synsets(lemma=_str)) > 0 else False


class TestsWordSearch(unittest.TestCase):
    def testEmptyDictionary(self):
        _dict = MySimpleDictionary([])
        self.assertEqual(len(word_search(['a', 'b'], _dict)), 0)

    def testEmptyGrid(self):
        _dict = MySimpleDictionary(['flower'])
        self.assertEqual(len(word_search([], _dict)), 0)

    def testSimpleDictionary(self):
        grid_chars = [['a', 'a', 'r'], ['t', 'c', 'd']]
        simple_dictionary = MySimpleDictionary(['car', 'card', 'cart', 'cat'])
        ground_truth = set(['cat', 'car', 'card'])
        self.assertEqual(word_search(grid_chars, simple_dictionary), ground_truth)

    def testExample(self):
        grid_chars = [['w', 'm', 'l'],
                      ['l', 'i', 'a'],
                      ['e', 'k', 'c']]
        dictionary = EnglishDictionary()
        ground_truth = set(['mile', 'i', 'aim', 'iw', 'lack', 'ia', 'milk', 'ca', 'mil', 'mak', 'el', 'lam', 'c',
                            'wi', 'kc', 'ai', 'la', 'ma', 'ml', 'cam', 'k', 'lek', 'ie', 'li', 'mac', 'ci', 'ka',
                            'mi', 'a', 'make', 'w', 'l', 'al', 'ki', 'le', 'm', 'lei', 'il', 'lac', 'cim', 'elk',
                            'cia', 'lm', 'elm', 'ic', 'ak', 'ali', 'mack', 'ac', 'ail', 'lie', 'am', 'e', 'ilk'])
        self.assertEqual(word_search(grid_chars, dictionary), ground_truth)


if __name__ == '__main__':
    unittest.main()

