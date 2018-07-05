#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque


def count_islands(n_rows: int, n_cols: int, grid: list) -> int:
    """
    Count the number of islands in a 2-D array.

    Two tiles belong to the same island if they are both land and are adjacent
    horizontally or vertically, but not diagonally.
    Solution: find an island cell, mark all its parts as water,
    proceed with remaining islands.

    Args:
        n_rows: Number of rows.
        n_cols: Number of columns.
        grid: 2-dimensional array of booleans, where false means water
        and true means land.

    Returns: The number of islands.

    """
    grid = grid.copy()
    n_islands = 0
    for row in range(n_rows):
        for col in range(n_cols):
            if not grid[row][col]:
                continue
            _traverse_island_bfs(row, col, grid, n_rows, n_cols)
            n_islands += 1
    return n_islands


def _traverse_island_bfs(row: int, col: int, grid: list, nrow: int,
                         ncol: int):
    """
    Mark island cells connected to the current (row, col) as False, using BFS.

    Args:
        row: Current row (x-index).
        col: Current col (y-index).
        grid: 2-D list of booleans.
        nrow: Number of rows in the grid.
        ncol: Number of columns in the grid.

    Returns: None

    """
    grid[row][col] = False
    q = deque([(row, col)])
    while q:
        curr_row, curr_col = q.popleft()
        for new_row, new_col in _neighbours(curr_row, curr_col, nrow, ncol):
            if not grid[new_row][new_col]:
                continue
            grid[new_row][new_col] = False
            q.append((new_row, new_col))


def _neighbours(row: int, col: int, nrow: int, ncol: int) -> (int, int):
    """Yield valid neighbours for a cell with indices (row, col)."""
    for delt_x, delt_y in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        next_row = row + delt_x
        next_col = col + delt_y
        if 0 <= next_row < nrow and 0 <= next_col < ncol:
            yield next_row, next_col
