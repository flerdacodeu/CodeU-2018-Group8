#Using Python 3

import unittest
from counting_islands import count_islands, neighbours, find_land

class TestSolver(unittest.TestCase):

    def test_example_solver(self):
        """
        Tests example test case given in assignment.
        """
        self.assertEqual(count_islands([[False, True, False, True], [True, True, False, False], [False, False, True, False], [False, False, True, False]]), 3)

    def test_no_water(self):
        """
        Tests case of no water on map. Should return 1 island.
        """
        self.assertEqual(count_islands([[True, True, True], [True, True, True], [True, True, True]]), 1)

    def test_no_islands(self):
        """
        Tests case of no islands, all water on map.
        """
        self.assertEqual(count_islands([[False, False, False], [False, False, False], [False, False, False]]), 0)

    def test_no_map(self):
        """
        Tests case of an empty map.
        """
        self.assertEqual(count_islands([]), 0)


if __name__ == "__main__":
    unittest.main()
