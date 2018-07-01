# Python 3
import unittest
from islands import *


class TestIslands(unittest.TestCase):
    def setUp(self):
        self.islandInstance = Islands(0, 0)

    def testEmptyGrid(self):
        self.islandInstance.traverse([])
        self.assertEqual(len(self.islandInstance), 0)

    def testSingle2TilesIsland(self):
        self.assertEqual(self.islandInstance.traverse([[False, True], [False, True]])[0],
                         set([1, 3]))
        self.assertEqual(len(self.islandInstance), 1)

    def testMultipleIslands(self):
        grid = [[False, False,  True,   False,  False],
                [True,  True,   True,   True,   True],
                [False, False,  False,  False,  False],
                [True,  False,  False,  False,  True],
                [True,  True,   False,  False,  False]]
        self.assertEqual(self.islandInstance.traverse(grid),
                         [set([2, 5, 6, 7, 8, 9]),
                          set([15, 20, 21]),
                          set([19])])
        self.assertEqual(len(self.islandInstance), 3)

if __name__ == '__main__':
    unittest.main()
