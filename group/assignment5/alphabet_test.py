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

if __name__ == '__main__':
    unittest.main()
