##########################################################################
# python 3
##########################################################################
import unittest
from q1_anagram_tatjana import *


class TestsAnagrams(unittest.TestCase):
    def setUp(self):
        pass

    def test1_empty_strings(self):
        self.assertEqual(anagrams('', ''), True)  # Default Assumption: empty strings are anagrams
        self.assertEqual(anagrams('', '', empty_strings_anagrams=False), False)
        self.assertEqual(anagrams('', '!!!'), True)

    def test2_anagrams(self):
        self.assertEqual(anagrams('listen', 'silent'), True)
        self.assertEqual(anagrams('ahahahah', 'hahahaha'), True)
        self.assertEqual(anagrams('maybe, yes, likely, no!', 'no, likely, maybe... yes!'), True)

    def test3_not_anagrams(self):
        self.assertEqual(anagrams('apple', 'pabble'), False)
        self.assertEqual(anagrams('asdfghjkl', 'qwertyuiop', case_sensitive=False), False)
        self.assertEqual(anagrams('ana mile', 'mile'), False)

    def test4_caseSensitive(self):
        self.assertEqual(anagrams('ana', 'AnA'), False)
        self.assertEqual(anagrams('ana', 'AnA', case_sensitive=False), True)


class TestAnagramsMemory(unittest.TestCase):
    def setUp(self):
        pass

    def test1_empty_strings(self):
        self.assertEqual(anagrams_memory('', ''), True)  # Default Assumption: empty strings are anagrams
        self.assertEqual(anagrams_memory('', '', empty_strings_anagrams=False), False)
        self.assertEqual(anagrams_memory('', '!!!'), True)

    def test2_anagrams(self):
        self.assertEqual(anagrams_memory('listen', 'silent'), True)
        self.assertEqual(anagrams_memory('ahahahah', 'hahahaha'), True)
        self.assertEqual(anagrams_memory('maybe, yes, likely, no!', 'no, likely, maybe... yes!'), True)

    def test3_not_anagrams(self):
        self.assertEqual(anagrams_memory('apple', 'pabble'), False)
        self.assertEqual(anagrams_memory('asdfghjkl', 'qwertyuiop', case_sensitive=False), False)
        self.assertEqual(anagrams_memory('ana mile', 'mile'), False)

    def test4_caseSensitive(self):
        self.assertEqual(anagrams_memory('ana', 'AnA'), False)
        self.assertEqual(anagrams_memory('ana', 'AnA', case_sensitive=False), True)


class TestSentenceAnagrams(unittest.TestCase):
    def setUp(self):
        pass

    def test1_empty_strings(self):
        self.assertEqual(sentence_anagrams('', ''), True)  # Default Assumption: empty strings are anagrams
        self.assertEqual(sentence_anagrams('', '', empty_strings_anagrams=False), False)
        self.assertEqual(sentence_anagrams('', '!!!'), True)

    def test2_anagrams(self):
        self.assertEqual(sentence_anagrams('listen', 'silent'), True)
        self.assertEqual(sentence_anagrams('ahahahah', 'hahahaha'), True)
        self.assertEqual(sentence_anagrams('maybe, yes, likely, no!', 'no, likely, maybe... yes!'), True)

    def test3_not_anagrams(self):
        self.assertEqual(sentence_anagrams('apple', 'pabble'), False)
        self.assertEqual(sentence_anagrams('asdfghjkl', 'qwertyuiop', case_sensitive=False), False)
        self.assertEqual(sentence_anagrams('ana mile', 'mile'), False)

    def test4_caseSensitive(self):
        self.assertEqual(sentence_anagrams('ana', 'AnA'), False)
        self.assertEqual(sentence_anagrams('ana', 'AnA', case_sensitive=False), True)
        self.assertEqual(sentence_anagrams('dnn ai 33 ml mile 33 AI NN', 'DNN AI 33 ml mile 33 AI NN'), False)  # case sensitive
        self.assertEqual(sentence_anagrams('dnn ai 33 ml mile 33 AI NN', 'DNN AI 33 ml mile 33 AI NN', case_sensitive=False), True)


if __name__ == '__main__':
    unittest.main()
