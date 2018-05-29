#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Assignment 1, Q1:
    "Given two strings, determine if one is an anagram of the other. Two words are anagrams of
    each other if they are made of the same letters in a different order.
    Optional Follow-ups:
    * Make the algorithm able to handle both case sensitive and case insensitive anagrams.
    * Make the algorithm able to handle anagrams of sentences, where each word in the resulting
    sentence is an anagram of one of the words in the original sentence."

My assumptions:
    1. For follow-up 2, let's say we are provided with some kind of sentence tokenizer (word segmenter).
    Based on the segmentation, punctuation can be omitted or treated as individual tokens.
    Now I am using the NLTK package for tokenization, and the solution is punctuation-sensitive (i.e., for two sentences
    to be anagrams, they should contain word-level anagrams and the same punctuation marks as well).
'''
from collections import Counter

from nltk.tokenize.moses import MosesTokenizer

tokenizer = MosesTokenizer()


def tokenize_sentence(s):
    '''
    Obtain word-level segmentation for a sentence.
    :param s: Sentence to segment.
    :return: List of words contained in the sentence.
    '''
    return tokenizer.tokenize(s)


def is_word_anagram(w1, w2, case_sensitive=False):
    '''
    "Given two strings, determine if one is an anagram of the other."
    The main idea of the solution is that anagrams have the same letters and an equal number of them.
    :param w1: First string to check against the second word w2.
    :param w2: Second string to check against the first word w1.
    :param case_sensitive: Boolean whether the anagram check should account for letter casing.
    :return: Boolean whether the two words are anagrams.
    '''
    if len(w1) != len(w2):
        return False
    if not case_sensitive:  # Follow-up #1
        w1 = w1.lower()
        w2 = w2.lower()
    return Counter(w1) == Counter(w2)


def is_sentence_anagram(s1, s2, case_sensitive=False):
    '''
    "Make the algorithm able to handle anagrams of sentences, where each word in the resulting
    sentence is an anagram of one of the words in the original sentence."

    :param s1: First string to check against the second sentence s2.
    :param s2: Second string to check against the first sentence s1.
    :param case_sensitive: Boolean whether the anagram check should account for letter casing.
    :return: Boolean, whether the two sentences are anagrams.
    '''
    words1 = tokenize_sentence(s1)  # obtaining word-level segmentation
    words2 = tokenize_sentence(s2)
    if len(words1) != len(words2):
        return False
    anagram_positions = [False] * len(words1)  # make sure that each word has its anagram counterpart in s2
    for i, word1 in enumerate(words1):  # O(n^2)
        for word2 in words2:
            if is_word_anagram(word1, word2, case_sensitive=case_sensitive):
                anagram_positions[i] = True
                break
        else:  # could not find any anagram for the current word1
            return False
    return all(anagram_positions)
