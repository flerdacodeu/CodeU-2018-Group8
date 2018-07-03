import unittest
import Task1


class TestTask(unittest.TestCase):

    def setUp(self):
        self.dictionary = ["CAR", "CARD", "CART", "CAT"]
        self.grid = ["AAR", "TCD"]
        self.dictionary2 = []
        self.grid2 = []
        self.found = []

    def test_example(self):
        self.assertItemsEqual(Task1.find_words(self.grid,self.dictionary), ["CAT", "CAR", "CARD"])

    def test_loops(self):
        self.assertItemsEqual(Task1.find_words(["AT"], ["ATA"]), [])

    def test_empty_dict_and_grid(self):
        self.assertItemsEqual(Task1.find_words(self.grid2, self.dictionary2), [])
        self.assertItemsEqual(Task1.find_words(self.grid2, self.dictionary), [])
        self.assertItemsEqual(Task1.find_words(self.grid, self.dictionary2), [])





