# python 3
import unittest
from alphabet import Alphabet


class TestAlphabet(unittest.TestCase):

    def testEmptyAlphabet(self):
        self.assertEqual(len(Alphabet(dict()).get()), 0)

    def testSimpleAlphabet(self):
        _dictionary = ['art', 'rat', 'cat', 'car']
        alphabet = Alphabet(_dictionary)
        ground_truth = [['a', 't', 'r', 'c'], ['t', 'a', 'r', 'c']]
        self.assertIn(alphabet.get(), ground_truth)

    def testAllSimpleAlphabets(self):
        _dictionary = ['art', 'rat', 'cat', 'car']
        alphabet = Alphabet(_dictionary)
        ground_truth = [['a', 't', 'r', 'c'], ['t', 'a', 'r', 'c']]
        self.assertCountEqual(alphabet.get_all(), ground_truth)

    def testConsistentDictionary(self):
        _dictionary = ['art', 'rat', 'cat', 'car']
        alphabet = Alphabet(_dictionary)
        self.assertEqual(len(alphabet.inconsistent()), 0)

    def testInconsistentDictionaryOneMinimalConstraint(self):
        _dictionary = ['art', 'rac', 'rat', 'ct', 'cat', 'car']
        alphabet = Alphabet(_dictionary)
        self.assertCountEqual(alphabet.graph.all_cycles(),
                              [['a', 'r', 'c', 't', 'a'],
                               ['a', 'c', 't', 'a'],
                               ['r', 'c', 't', 'r']])
        self.assertCountEqual(alphabet.inconsistent(), ['c->t'])

    def testInconsistentDictionaryTwoMinimalConstraints(self):
        _dictionary = ['art', 'ant', 'racket', 'rat', 'can', 'cat', 'car']
        alphabet = Alphabet(_dictionary)
        self.assertCountEqual(alphabet.graph.all_cycles(),
                              [['r', 'n', 't', 'r'],
                               ['r', 'n', 'r'],
                               ['r', 'c', 't', 'r']])
        self.assertCountEqual(alphabet.inconsistent(), ['r->n', 'r->c'])

if __name__ == '__main__':
    unittest.main()
