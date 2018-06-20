import unittest
import Task1


class TestTask(unittest.TestCase):
    """Unit tests for Task1"""
    def test_find_words(self):    # testing for an existing element
        Task1.find_words(0, 0)
        self.assertEqual(Task1.found, [])
        Task1.find_words(1, 1)
        self.assertItemsEqual(Task1.found, ['CAT', 'CARD', 'CAR'])

    def test_find_word_with_ind_out_of_range(self):   # testing for non-existent elements
        self.assertEquals(Task1.find_words(-1, -1), False)
        self.assertEquals(Task1.find_words(0, 5), False)
        self.assertEqual(Task1.found, [])

    def test_main(self):    # testing for every element using the example from the assignment
        Task1.main()
        self.assertItemsEqual(Task1.found, ['CAT', 'CARD', 'CAR'])
