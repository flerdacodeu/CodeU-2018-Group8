def _normalize(s, case_sensitive=True, punctuation="none"):
    """
    Normalize the string according to parameters case_sensitive and punctuation.
    :param string: initial string
    :param case_sensitive: bool (default True)
        False -- all letters will be converted in lowercase
        True -- all letters will not be changed
    :param punctuation: one of ["ignore", "none", "space"] default ("none")
        "none" -- all punctuation marks will be considered as letters
        "ignore" -- all punctuation marks will be removed from the string
        "spaces" -- all punctuation marks will be converted to spaces
    :return: normalized string
    """
    if not case_sensitive:
        s = s.lower()
    if punctuation == "spaces":
        s = ''.join([c if c.isalpha() else ' ' for c in s])
    elif punctuation == "ignore":
        s = ''.join([c for c in s if c.isalpha() or c == ' '])
    return s


def sorted_letters(s):
    """
    Sort letters in each word and words in sentence s.
    :param s: initial string, word or sentence
    :return: list, sorted list of words from s with sorted letters
    """
    return sorted(map(sorted, s.split()))


def is_anagram(s1, s2, case_sensitive=True, punctuation="none"):
    """
    Check whether strings are anagrams according to parameters case_sensitive and punctuation.
    :param s1, s2: Initial strings.
    :param case_sensitive: bool (default True)
        False -- all letters will be converted in lowercase
        True -- all letters will not be changed
    :param punctuation: one of ["ignore", "none", "space"] default ("none")
        "none" -- all punctuation marks will be considered as letters
        "ignore" -- all punctuation marks will be removed from the string
        "spaces" -- all punctuation marks will be converted to spaces
    :return: bool
        True if strings are anagrams, else False
    """
    s1 = _normalize(s1, case_sensitive=case_sensitive, punctuation=punctuation)
    s2 = _normalize(s2, case_sensitive=case_sensitive, punctuation=punctuation)

    if len(s1) != len(s2):
        return False

    return sorted_letters(s1) == sorted_letters(s2)

#Next function implemented for compare real working time of two functions. The function can work only with words.
from collections import Counter
def is_anagram_linear(s1, s2):
    """
    Check whether two words are anagrams using Counter. Function have a linear asymptotic.
    Words consist only letters.
    :param s1, s2: inititial words
    :return: bool
        True if strings are anagrams, else False
    """
    return Counter(s1) == Counter(s2)
