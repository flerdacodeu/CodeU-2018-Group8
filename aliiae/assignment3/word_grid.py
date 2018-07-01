#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Given a grid of letters and a dictionary,
find all the words from the dictionary that can be formed in the grid.
Your function receives the grid and the dictionary.
You should return the set of all words found.

Assumptions:
    1. Return an empty set() if there are no words found in the grid.
    2. The input strings are not preprocessed (e.g., lowercased), so it is up to
    the user how to maintain consistency.
"""


class LetterGrid:
    def __init__(self, letters, nrow, ncol):
        """
        Initialize a (ncol x nrow) grid containing given letters.

        Implemented as a 2-D list.

        Args:
            letters: List of elements to put into the grid, left-to-right.
            nrow: Number of rows in the grid.
            ncol: Number of columns in the grid.
        """
        if len(letters) != ncol * nrow:
            raise ValueError(
                f'Can\'t form {ncol}x{nrow} grid out of {len(letters)} chars.')
        letters = list(letters)
        self.grid = [letters[idx:idx + ncol]
                     for idx in range(0, len(letters), ncol)]
        self.ncol = ncol
        self.nrow = nrow

    def __str__(self):
        return '\n'.join(' '.join(row) for row in self.grid)

    def find_words_from_dict(self, dictionary):
        """
        Return the set of all words found in the grid, based on a dictionary.

        The idea is to try different starting cells in a grid and collect all
        valid words that can be constructed from the starting point (via DFS).
        Duplicate words will be eliminated when added to the set.

        Args:
            dictionary: Dictionary containing words and providing is_word and
            is_prefix functions.

        Returns: Set of all words found in the grid, or an empty set if no words
        found.

        """
        results = set()
        for row in range(self.nrow):
            for col in range(self.ncol):
                start_letter = self.grid[row][col]
                results.update([''.join(letters)
                                for letters in
                                self._collect_words(row, col, dictionary,
                                                    [start_letter], set())])
        return results

    def _collect_words(self, row, col, dictionary, letters, visited):
        """
        Recursively explore the grid from starting point and yield valid words.

        Args:
            row: Index of the starting row.
            col: Index of the starting column.
            dictionary: Dictionary containing words and providing is_word and
            is_prefix functions.
            letters: List of letters, the prefix being currently constructed.
            visited: Set of visited cells.

        Yields: List of letters representing a found word.

        """
        if not dictionary.is_prefix(letters) or (row, col) in visited:
            return
        if dictionary.is_word(letters):
            yield letters
        visited.add((row, col))
        for next_row, next_col in self._neighbours(row, col):
            next_letters = letters + [self.grid[next_row][next_col]]
            yield from self._collect_words(next_row, next_col, dictionary,
                                           next_letters, visited)
        visited.remove((row, col))

    def _neighbours(self, row, col):
        """Yield valid adjacent indices for the cell [row, col]."""
        for delt_x, delt_y in ((x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)):
            next_row = row + delt_x
            next_col = col + delt_y
            if (0 <= next_row < self.nrow and 0 <= next_col < self.ncol
                    and (next_row, next_col) != (row, col)):
                yield next_row, next_col
