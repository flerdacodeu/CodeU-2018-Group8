#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import time

from trie import Trie
from word_grid import LetterGrid


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.start_time = time.time()
        self.word_list = 'CAR, CARD, CART, CAT'.lower().split(', ')
        self.grid = LetterGrid('AARTCD'.lower(), nrow=2, ncol=3)
        self.dictionary = Trie(self.word_list)

    def tearDown(self):
        # how much time each test takes
        t = time.time() - self.start_time
        print(f'{self.id()}: {t:.3f}')

    def test_grid_init(self):
        self.assertEqual([['a', 'a', 'r'], ['t', 'c', 'd']], self.grid.grid)
        self.assertRaises(ValueError, LetterGrid, 'abc', 2, 3)
        self.assertRaises(ValueError, LetterGrid, '', 0, 0)

    def test_grid_print(self):
        self.assertEqual('a a r\nt c d', str(self.grid))

    def test_grid_find_words(self):
        correct_words = set('CAR, CARD, CAT'.lower().split(', '))
        self.assertCountEqual(correct_words,
                              self.grid.find_words_from_dict(self.dictionary))

    def test_grid_find_words_extended(self):
        self.dictionary.insert_words(['act', 'rad', 'rat'])
        correct_words = set('CAR, CARD, CAT, act, rad, rat'.lower().split(', '))
        self.assertCountEqual(correct_words,
                              self.grid.find_words_from_dict(self.dictionary))

    def test_grid_no_words_found(self):
        grid = LetterGrid('a', nrow=1, ncol=1)
        self.assertCountEqual(set(), grid.find_words_from_dict(self.dictionary))

    def test_grid_repeating_same_cell(self):
        dictionary = Trie(['cara'])
        self.assertCountEqual(set(), self.grid.find_words_from_dict(dictionary))

    def test_grid_bigger_grid(self):
        words = 'you shall know a word by the company it keeps'.split()
        dictionary = Trie(words)
        nrow = ncol = 6
        grid = LetterGrid(''.join(words), nrow=nrow, ncol=ncol)
        self.assertCountEqual({'you', 'know', 'a', 'word', 'the', 'keeps'},
                              grid.find_words_from_dict(dictionary))

    def test_grid_large_grid(self):
        max_word_len = 4
        self.dictionary.insert_words(['a' * k for k in range(1, max_word_len)])
        nrow = ncol = 100
        grid = LetterGrid(['a'] * (nrow * ncol), nrow=nrow, ncol=ncol)
        self.assertCountEqual({'a' * k for k in range(1, max_word_len)},
                              grid.find_words_from_dict(self.dictionary))


if __name__ == '__main__':
    unittest.main()
