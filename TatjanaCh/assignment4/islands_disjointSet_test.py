# Python 3
import unittest
from islands_disjointSet import Islands


class TestIslands(unittest.TestCase):

    def testEmptyGrid(self):
        self.assertRaises(ValueError, lambda: Islands([]))

    def testSingle2TilesIsland(self):
        grid = [[False, True], [False, True]]
        islands = Islands(grid)
        self.assertEqual(islands.get_sets(), [set([1, 3])])
        self.assertEqual(len(islands), 1)

    def testMultipleIslands(self):
        grid = [[False, False,  True,   False,  False],
                [True,  True,   True,   True,   True],
                [False, False,  False,  False,  False],
                [True,  False,  False,  False,  True],
                [True,  True,   False,  False,  False]]
        islands = Islands(grid)
        ground_truth = [set([2, 5, 6, 7, 8, 9]),
                        set([15, 20, 21]),
                        set([19])]
        self.assertEqual(islands.get_sets(), ground_truth)
        self.assertEqual(len(islands), len(ground_truth))

    def testNewEdgeMergesExistingIslands(self):
        grid = [[False, False,  True,   False,  False],
                [True,  True,   True,   True,   True],
                [False, False,  False,  False,  False],
                [True,  False,  True,   False,  True],
                [True,  True,   True,  False,  False]]
        islands = Islands(grid)
        ground_truth = [set([2, 5, 6, 7, 8, 9]),
                        set([15, 17, 20, 21, 22]),
                        set([19])]
        self.assertEqual(islands.get_sets(), ground_truth)
        self.assertEqual(len(islands), len(ground_truth))

if __name__ == '__main__':
    unittest.main()
