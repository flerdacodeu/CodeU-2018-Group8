#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Optional follow-up​:
Implement a dictionary class that can be constructed from a list of words.

A dictionary class with these two methods:
* isWord(string): Returns whether the given string is a valid word.
* isPrefix(string): Returns whether the given string is a prefix of at least one
word in the dictionary.

Assumptions:
    The dictionary is a trie implemented as node objects with children stored in
    a hashmap.
"""
from collections import defaultdict


class Trie:
    def __init__(self, words=None):
        """
        Implement a trie node that has trie children and bool if it ends a word.

        Args:
            words: A list of words that can be inserted into the trie.
        """
        self.children = defaultdict(Trie)
        self._is_word_end = False
        if words:
            self.insert_words(words)

    def __str__(self):
        return ' '.join(self.children)

    def insert_words(self, words):
        """
        Insert a list of words into the trie.
        Args:
            words: A list of words to be inserted into the trie.

        Returns: None

        """
        for word in words:
            self.insert_word(word)

    def insert_word(self, word):
        """
        Insert a word into the trie.
        Args:
            word: A word to be inserted into the trie.

        Returns: None

        """
        current = self
        for letter in word:
            current = current.children[letter]
        current._is_word_end = True

    def is_word(self, word):
        """
        Return whether the given string is a valid word.
        Args:
            word: The word to look for.

        Returns: True if the word is found, else False.

        """
        current = self
        for letter in word:
            if letter in current.children:
                current = current.children[letter]
            else:
                return False
        else:
            return current._is_word_end

    def is_prefix(self, prefix):
        """
        Return whether the given string is a prefix of at least one word.
        Args:
            prefix: Prefix to search for in the trie.

        Returns: True if the string is a prefix of a word, else False.

        """
        current = self
        for letter in prefix:
            if letter in current.children:
                current = current.children[letter]
            else:
                return False
        else:
            return True
