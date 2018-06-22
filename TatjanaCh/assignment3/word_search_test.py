# Python 3
import unittest
import sys
from nltk.corpus import wordnet
from word_search import *


class MySimpleDictionary(Dictionary):
    """
    A dictionary that assumes storage of only few words. 
    It is used for testing and 'isPrefix' is not optimized.
    """
    def __init__(self, words):
        self.words = set(words)

    def isWord(self, _str):
        """
        Returns whether the given string is a valid word. Not case sensitive
        :param _str: [string]
        :return: [bool] True/False
        """
        return True if _str in self.words else False

    def isPrefix(self, _str):
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

    def isWord(self, _str):
        """
        Returns whether the given string is a valid word. Not case sensitive
        :param _str: [string]
        :return: [bool] True/False
        """
        return True if wordnet.synsets(_str) else False

    def isPrefix(self, _str):
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
        self.assertEqual(len(wordSearch(['a', 'b'], _dict)), 0)

    def testEmptyGrid(self):
        _dict = MySimpleDictionary(['flower'])
        self.assertEqual(len(wordSearch([], _dict)), 0)

    def testSimpleDictionary(self):
        grid_chars = [['a', 'a', 'r'], ['t', 'c', 'd']]
        simpleDictionary = MySimpleDictionary(['car', 'card', 'cart', 'cat'])
        groundTruthDict = set(['cat', 'car', 'card'])
        self.assertEqual(len(wordSearch(grid_chars, simpleDictionary) & groundTruthDict),
                         len(groundTruthDict))

    def testExample(self):
        grid_chars = [['w', 'm', 'l'],
                      ['l', 'i', 'a'],
                      ['e', 'k', 'c']]
        Dictionary = EnglishDictionary()
        groundTruthDict = set(['mile', 'i', 'aim', 'iw', 'lack', 'ia', 'milk', 'ca', 'mil', 'mak', 'el', 'lam', 'c',
                               'wi', 'kc', 'ai', 'la', 'ma', 'ml', 'cam', 'k', 'lek', 'ie', 'li', 'mac', 'ci', 'ka',
                               'mi', 'a', 'make', 'w', 'l', 'al', 'ki', 'le', 'm', 'lei', 'il', 'lac', 'cim', 'elk',
                               'cia', 'lm', 'elm', 'ic', 'ak', 'ali', 'mack', 'ac', 'ail', 'lie', 'am', 'e', 'ilk'])
        self.assertEqual(len(wordSearch(grid_chars, Dictionary) & groundTruthDict),
                         len(groundTruthDict))


if __name__ == '__main__':
    unittest.main()

