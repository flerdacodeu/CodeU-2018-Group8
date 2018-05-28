##########################################################################
# python 3
##########################################################################
import re
from collections import defaultdict


def letters_occurrences(_str, _dict=None, inc=1):
    """
    Counts the occurrences of the unique letters in the input string.
    :param _str: [string]
    :param _dict: [dict, optional] dictionary whose keys are letters and values integers. Default: None
    :param inc: [int, optional] Increment/Decrement value for each occurrence. Default: 1
    :return: dictionary whose keys are the encountered letters and values their occurrences
    """
    _dict = _dict if _dict is not None else defaultdict(int)

    for char in _str:
        _dict[char] += inc
    return _dict


def anagrams(s1, s2, case_sensitive=True, empty_strings_anagrams=True):
    """
    Determines if two input strings are anagrams. Two words are anagrams, if they consist of the same letters and 
    numbers, irrespective of their order or extra non alphanumeric characters.
    :param s1: [string] 
    :param s2: [string]
    :param case_sensitive: [bool, optional] case sensitive. Default: True
    :param empty_strings_anagrams: [bool, optional] If True, two empty strings (or having only non alphanumeric 
    characters) are considered anagrams. Default: True
    :return: [bool]
    """
    if not case_sensitive:
        s1 = s1.lower()
        s2 = s2.lower()

    s1 = re.sub(r'\W+', '', s1)
    s2 = re.sub(r'\W+', '', s2)

    if len(s1) != len(s2):  # to avoid computation
        return False
    elif len(s1) == len(s2) == 0:
        if empty_strings_anagrams:
            return True
        else:
            return False

    dict_s1 = letters_occurrences(s1)  # O(|s1|)
    dict_s2 = letters_occurrences(s2)  # O(|s2|)

    if len(dict_s1) != len(dict_s2):
        return False
    for key in dict_s1:  # O(|dict_s1|) <-> O(|dict_s1|), worst case max(O(|s1|), O(|s2|))
        if key not in dict_s2 or dict_s1[key] != dict_s2[key]:
            return False

    return True  # max(O(|s1|), O(|s2|))


def anagrams_memory(s1, s2, case_sensitive=True, empty_strings_anagrams=True):
    """
    Determines if two input strings are anagrams. Two words are anagrams, if they consist of the same letters and 
    numbers, irrespective of their order or extra non alphanumeric characters.
    Note: The implementation uses one dictionary.
    :param s1: [string] 
    :param s2: [string]
    :param case_sensitive: [bool, optional] case sensitive. Default: True
    :param empty_strings_anagrams: [bool, optional] If True, two empty strings (or having only non alphanumeric 
    characters) are considered anagrams. Default: True
    :return: [bool]
    """
    if not case_sensitive:
        s1 = s1.lower()
        s2 = s2.lower()

    s1 = re.sub(r'\W+', '', s1)
    s2 = re.sub(r'\W+', '', s2)

    if len(s1) != len(s2):  # to avoid computation
        return False
    elif len(s1) == len(s2) == 0:
        if empty_strings_anagrams:
            return True
        else:
            return False

    common_dict = letters_occurrences(s2, _dict=letters_occurrences(s1), inc=-1)

    for _, value in common_dict.items():
        if value != 0:
            return False
    return True


def sentence_anagram_of(s1, s2, case_sensitive=True, empty_strings_anagrams=True):
    """
    Returns true if each word of the second sentence is an anagram-word of the first.
    
    Assumption: words are separated by whitespace(s), \n, \t
    :param s1: [str]
    :param s2: [str]
    :param case_sensitive: [bool, optional] case sensitive. Default: True
    :param empty_strings_anagrams: [bool, optional] If True, two empty strings (or having only non alphanumeric 
    characters) are considered anagrams. Default: True
    :return: [bool] 
    """
    words1 = s1.split()
    words2 = s2.split()

    for w2 in words2:
        found_anagram = False
        for w1 in words1:
            if anagrams(w1, w2, case_sensitive=case_sensitive,
                        empty_strings_anagrams=empty_strings_anagrams):
                found_anagram = True
                break
        if not found_anagram:
            return False
    return True


def sentence_anagrams(s1, s2, case_sensitive=True, empty_strings_anagrams=True):
    """
    Returns true if each word of one of the input sentences is an anagram-word 
    of at least one of the words of the other, and vice-versa.

    Assumption: words are separated by whitespace(s), \n, \t
    :param s1: [str]
    :param s2: [str]
    :param case_sensitive: [bool, optional] case sensitive. Default: True
    :param empty_strings_anagrams: [bool, optional] If True, two empty strings (or having only non alphanumeric 
    characters) are considered anagrams. Default: True
    :return: [bool]
    """
    s1 = re.sub(r'[^\s\w]+', '', s1)
    s2 = re.sub(r'[^\s\w]+', '', s2)

    if len(s1) != len(s2):  # to avoid computation
        return False
    elif len(s1) == len(s2) == 0:
        if empty_strings_anagrams:
            return True
        else:
            return False

    return sentence_anagram_of(s1, s2,
                               case_sensitive=case_sensitive,
                               empty_strings_anagrams=empty_strings_anagrams) and \
           sentence_anagram_of(s2, s1,
                               case_sensitive=case_sensitive,
                               empty_strings_anagrams=empty_strings_anagrams)
