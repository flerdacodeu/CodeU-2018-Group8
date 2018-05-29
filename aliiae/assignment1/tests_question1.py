#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from question1 import is_word_anagram, is_sentence_anagram


class TestAnagrams(unittest.TestCase):
    def test_empty_strings(self):
        self.assertTrue(is_word_anagram('', ''))

    def test_empty_cased_strings(self):
        self.assertTrue(is_word_anagram('', '', case_sensitive=True))

    def test_true_anagrams(self):
        self.assertTrue(is_word_anagram('listen', 'silent'))
        self.assertTrue(is_word_anagram('triangle', 'integral'))

    def test_false_anagrams(self):
        self.assertFalse(is_word_anagram('apple', 'pabble'))

    def test_false_anagrams_diff_len(self):
        self.assertFalse(is_word_anagram('listen', 'silentt'))

    def test_false_anagrams_extra_letter(self):
        self.assertFalse(is_word_anagram('listen', 'sileen'))

    def test_case_sensitive(self):
        self.assertFalse(is_word_anagram('Triangle', 'Integral', case_sensitive=True))

    def test_sentence_anagrams(self):
        self.assertTrue(is_sentence_anagram('hello, world!', 'lHloe! rwodl,', case_sensitive=False))

    def test_sentence_anagrams_cased(self):
        self.assertFalse(is_sentence_anagram('hello, world!', 'lHloe! rwodl,', case_sensitive=True))

    def test_sentence_anagrams_extra_letter(self):
        self.assertFalse(is_sentence_anagram('Hello, world!', 'Hello, worlds!'))


if __name__ == '__main__':
    unittest.main()
