# Python 3
import unittest
from utils import neighbors


class TestNeighbors(unittest.TestCase):
    def testZeroes(self):
        self.assertRaises(ValueError, lambda: neighbors(0, 0, 0, 0))

    def testNegativeInput(self):
        self.assertRaises(ValueError, lambda: neighbors(4, 5, -1, 5))
        self.assertRaises(ValueError, lambda: neighbors(4, 5, 5, -1))

    def testSamePosition(self):
        self.assertFalse(neighbors(2, 2, width=3, height=3))

    def testConsecutiveButNotNeighbors(self):
        self.assertFalse(neighbors(2, 3, width=3, height=2))

    def testDiagonallyNotNeighbors(self):
        self.assertFalse(neighbors(2, 4, width=3, height=3))

    def testVerticalNeighbors(self):
        self.assertTrue(neighbors(2, 5, width=3, height=3))

    def testHorizontalNeighbors(self):
        self.assertTrue(neighbors(4, 5, width=3, height=3))

if __name__ == '__main__':
    unittest.main()
