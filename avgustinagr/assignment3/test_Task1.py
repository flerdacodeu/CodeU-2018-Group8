import unittest
import task

class TestTask(unittest.TestCase):

    def setUp(self):
        self.dictionary = ["CAR", "CARD", "CART", "CAT"]
        self.grid = ["AAR", "TCD"]
        self.found = []

    def test_example(self):
        self.assertItemsEqual(task.main(self.grid,self.dictionary), ["CAT", "CAR", "CARD"])

    def test_loops(self):
        self.assertItemsEqual(task.main(["AT"], ["ATA"]), [])

    def test_find_word_with_ind_out_of_range(self):
        self.assertEquals(task.find_words(-1, -1, self.grid, self.dictionary, self.found), False)
        self.assertEquals(task.find_words(0, 5, self.grid, self.dictionary, self.found), False)



