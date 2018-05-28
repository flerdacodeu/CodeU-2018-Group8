##########################################################################
# python 3
##########################################################################
import unittest
# from q1_anagram_tatjana import anagrams as f
# from q1_anagram_tatjana import anagrams_memory as f
from q1_anagram_tatjana import sentence_anagrams as f


class TestsAnagram(unittest.TestCase):
    def setUp(self):
        pass

    def test1_empty_strings(self):
        """
        Assumption: empty strings are anagrams
        :return: 
        """
        self.assertEqual(f('', ''), True)

    def test2_empty_strings(self):
        self.assertEqual(f('', '', empty_strings_anagrams=False), False)

    def test3_empty_strings(self):
        self.assertEqual(f('', '!!!'), True)

    def test4_anagrams(self):
        self.assertEqual(f('listen', 'silent'), True)

    def test5_anagrams(self):
        self.assertEqual(f('ahahahah', 'hahahaha'), True)

    def test6_anagrams(self):
        self.assertEqual(f('maybe, yes, likely, no!', 'no, likely, maybe... yes!'), True)

    def test7_not_anagrams(self):
        self.assertEqual(f('apple', 'pabble'), False)

    def test8_not_anagrams(self):
        self.assertEqual(f('ana', 'AnA'), False)  # caseSensitive

    def test9_anagrams(self):
        self.assertEqual(f('ana', 'AnA', case_sensitive=False), True)

    def test10_not_anagrams(self):
        self.assertEqual(f('asdfghjkl', 'qwertyuiop', case_sensitive=False), False)

    def test11(selfs):
        selfs.assertEqual(f('ana mile', 'mile'), False)

    def test12(selfs):
        selfs.assertEqual(f('dnn ai 33 ml mile 33 AI NN', 'DNN AI 33 ml mile 33 AI NN'), False)  # case sensitive

    def test13(selfs):
        selfs.assertEqual(f('dnn ai 33 ml mile 33 AI NN', 'DNN AI 33 ml mile 33 AI NN', case_sensitive=False), True)


if __name__ == '__main__':
    unittest.main()
