#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.word_list = 'CAR, CARD, CART, CAT'.lower().split(', ')
        self.dictionary = Trie(self.word_list)

    def test_trie_empty_word(self):
        self.assertFalse(self.dictionary.is_word([]))

    def test_trie_node_is_word(self):
        for word in self.word_list:
            self.assertTrue(self.dictionary.is_word(word))

    def test_trie_node_is_not_word(self):
        for non_word in ['c', 'ca', 'cards']:
            self.assertFalse(self.dictionary.is_word(non_word))

    def test_trie_prefix_is_prefix(self):
        for prefix in 'C, CA, CAR, CARD, CART, CAT'.lower().split(', '):
            self.assertTrue(self.dictionary.is_prefix(prefix))

    def test_trie_word_is_prefix(self):
        for word in self.word_list:
            self.assertTrue(self.dictionary.is_prefix(word))

    def test_trie_print(self):
        self.assertEqual('c', str(self.dictionary))


if __name__ == '__main__':
    unittest.main()
