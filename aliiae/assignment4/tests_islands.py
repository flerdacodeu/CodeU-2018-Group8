#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import unittest

from islands import count_islands


class TestIslands(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        # show execution time
        t = time.time() - self.startTime
        print(f'{self.id()}: {t:.3f}')

    def test_empty_grid(self):
        self.assertEqual(0, count_islands(0, 0, []))

    def test_simple_grid(self):
        ncol = nrow = 4
        grid = [[False] * ncol for _ in range(nrow)]
        true_indices = [(0, 1), (0, 3), (1, 0), (1, 1), (2, 2), (3, 2)]
        for row, col in true_indices:
            grid[row][col] = True
        self.assertEqual(3, count_islands(nrow, ncol, grid))

    def test_grid_is_island_itself(self):
        ncol = nrow = 30
        grid = [[True] * ncol for _ in range(nrow)]
        self.assertEqual(1, count_islands(nrow, ncol, grid))

    def test_grid_no_islands(self):
        ncol = nrow = 4
        grid = [[False] * ncol for _ in range(nrow)]
        self.assertEqual(0, count_islands(nrow, ncol, grid))


if __name__ == '__main__':
    unittest.main()
