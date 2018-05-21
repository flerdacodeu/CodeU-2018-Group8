# Created on 21.05.18, by Tatjana
# tatjana.chavdarova@{epfl,idiap}.ch
##########################################################################
# Assumption: only letters are considered (white space & punct. are ignored)
# Assumption: empty strings are anagrams
# python 3
##########################################################################
import time
import re


def letters_occurrences(_str):
    _dict = {}
    for l in _str:
        if l not in _dict:
            _dict[l] = 1
        else:
            _dict[l] += 1
    return _dict


def anagrams(s1, s2, case_sensitive=True):
    if not case_sensitive:
        s1 = s1.lower()
        s2 = s2.lower()

    s1 = re.sub(r'\W+', '', s1)
    s2 = re.sub(r'\W+', '', s2)

    # if empty strings are *not* anagrams, uncomment:
    # if 0 in [len(s1), len(s2)]:
    #     return False

    if len(s1) != len(s2):  # to avoid computation
        return False

    dict_s1 = letters_occurrences(s1)  # O(|s1|)
    dict_s2 = letters_occurrences(s2)  # O(|s2|)

    if len(dict_s1) != len(dict_s2):
        return False
    for key in dict_s1:  # O(|dict_s1|) <-> O(|dict_s1|), worst case max(O(|s1|), O(|s2|))
        if key not in dict_s2 or dict_s1[key] != dict_s2[key]:
            return False

    return True  # max(O(|s1|), O(|s2|))

##########################################################################
stime = time.time()

test_cases = []  # each element: str1, str2, caseSensitive, label
test_cases.append(['', '', None, True])  # assumption: empty strings are anagrams
test_cases.append(['...', '!!!', None, True])  # assumption: empty strings are anagrams
test_cases.append(['listen', 'silent', None, True])
test_cases.append(['triangle', 'integral', None, True])
test_cases.append(['apple', 'pabble', None, False])
test_cases.append(['ahahahah', 'hahahaha', None, True])
test_cases.append(['maybe, yes, likely, no!', 'no, likely, maybe...yes!', None, True])
test_cases.append(['ana', 'AnA', True, False])  # caseSensitive
test_cases.append(['ana', 'AnA', False, True])  # not caseSensitive


correct = 0
for test in test_cases:
    ans = anagrams(s1=test[0], s2=test[1], case_sensitive=test[2])
    if ans == test[3]:
        correct += 1
    else:
        print('Wrong answer for \'%s\' and \'%s\': %s' % (test[0], test[1], 'yes' if ans else 'no'))
print('Correct/Total: %d/%d' % (correct, len(test_cases)))

print('Took %fs' % (time.time() - stime))

##########################################################################
# Follow up 2: each word of str2 should be anagram of at least one of the
# words of str1.
# Assumption1: words are separated by whitespace(s), \n, \t
# Assumption2: if one of the sentences is empty string, the alg.returns false
# Assumption3: if the second sentence has no alphanum characters, returns True


def sentence_anagrams(s1, s2, case_sensitive=True):
    if 0 in [len(s1), len(s2)]:
        return False

    if not case_sensitive:
        s1 = s1.lower()
        s2 = s2.lower()

    s1 = re.sub(r'[^\s\w]+', '', s1)
    s2 = re.sub(r'[^\s\w]+', '', s2)

    words1 = s1.split()
    words2 = s2.split()

    if len(words2) == 0:
        return True  # Assumption3

    for w2 in words2:
        found_anagram = False
        for w1 in words1:
            if anagrams(w1, w2):
                found_anagram = True
                break
        if not found_anagram:
            return False
    return True

print('\nFollow up 2 ----------------------------------------------')
s1, s2 = 'ana mile', 'mile'
print(s1, '---', s2, '--->\t', sentence_anagrams(s1, s2))  # true

s1, s2 = '', ''
print(s1, '---', s2, '--->\t', sentence_anagrams(s1, s2))  # false

s1, s2 = 'aha', '!!!'
print(s1, '---', s2, '--->\t', sentence_anagrams(s1, s2))  # true

s1, s2 = 'ana mile1 dada ', 'mile'
print(s1, '---', s2, '--->\t', sentence_anagrams(s1, s2))  # false

s1, s2 = 'ai mile', 'ai ml nn DNN'
print(s1, '---', s2, '--->\t', sentence_anagrams(s1, s2))  # false

s1, s2 = 'dnn ai 33 ml mile 33 AI NN', 'ai ml nn DNN 33'
print(s1, '---', s2, '--->\t', sentence_anagrams(s1, s2))  # false (case sensitive)

s1, s2 = 'dnn ai 33 ml mile 33 AI NN', 'ai ml nn DNN 33'
print(s1, '---', s2, '--->\t', sentence_anagrams(s1, s2, case_sensitive=False))  # true (not case sensitive)