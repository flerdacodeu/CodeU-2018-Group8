#Using Python 3

import unittest
from word_search import Dictionary, WordSearch

class TestSolver(unittest.TestCase):

    def setUp(self):
        """
        Setting up test word search and dictionary from assignment example.
        """
        #FIrst test case (Example Given)
        self.test_word_search = WordSearch([["A", "A", "R"], ["T", "C", "D"]])
        self.test_dictionary = Dictionary(["CAR", "CARD", "CART", "CAT"])

        #Second Test Case (ONly one line in word search)
        self.test_ws_2 = WordSearch([["A", "C", "T"]])
        self.test_dict_2 = Dictionary(["ACT", "CAT", "AT"])

        #Third test case (Uses first case's word search, no results)
        self.test_dict_3 = Dictionary(["HAM"])

    def test_example_solver(self):
        """
        Tests example test case given in assignment.
        """
        self.assertEqual(self.test_word_search.find_words(self.test_dictionary), set(["CAR", "CARD", "CAT"]))

    def test_one_line_word_search(self):
        """
        Tests case of correct letters but not correct order because word search is only one line.
        """
        self.assertEqual(self.test_ws_2.find_words(self.test_dict_2), set(["ACT"]))

    def test_no_results(self):
        """
        Tests case of no results.
        """
        self.assertEqual(self.test_word_search.find_words(self.test_dict_3), set())



if __name__ == "__main__":
    unittest.main()
