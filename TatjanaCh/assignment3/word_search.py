# Python 3
from abc import ABCMeta, abstractmethod


class Dictionary(metaclass=ABCMeta):
    """
    Abstract Base Class, forcing derived classes to implement 'is_word' & 'is_prefix'
    """

    @abstractmethod
    def is_word(self, _str):
        pass

    @abstractmethod
    def is_prefix(self, _str):
        pass


class WordSearch:
    def __init__(self, grid, dictionary):
        """
        
        :param grid: [2D array of chars]
        :param dictionary: [class Dictionary] which has methods 'is_word' & 'is_prefix'
        """
        self.grid = grid
        self.dictionary = dictionary
        self.n_rows = len(grid)
        self.n_columns = len(grid[0]) if len(grid) > 0 else 0

    def __getitem__(self, item):
        """
        
        :param item: [tuple of integers] row, column
        :return: [char]
        """
        return self.grid[item[0]][item[1]]

    def __len__(self):
        return len(self.grid)

    def neighbors(self, i, j):
        """
        A generator that yields neighbors which are not visited
        :param i: [int]
        :param j: [int]
        :return: [tuple of integers] which correspond to row, column 
        """
        for ii in range(max(i - 1, 0), min(i + 2, self.n_rows)):
            for jj in range(max(j - 1, 0), min(j + 2, self.n_columns)):
                yield ii, jj

    def words_starting_at(self, i, j, visited, sub_word=''):
        """
        Given a grid of letters and a dictionary, it returns all the words from the dictionary 
        that can be formed starting from char (i, j) in the grid (without repetition)
        :param i: [int]
        :param j: [int]
        :param sub_word: [ str ]
        :param visited: [ 2D array of bool] True and False denote visited and not visited letter, respectively
        :return: [set]  of words
        """
        words = set()
        if visited[i][j]:
            return words

        sub_word += self[i, j]
        visited[i][j] = True

        if self.dictionary.is_word(sub_word):
            words.add(sub_word)

        if self.dictionary.is_prefix(sub_word):
            for ii, jj in self.neighbors(i, j):
                words.update(self.words_starting_at(i=ii, j=jj, visited=visited, sub_word=sub_word[:]))
        visited[i][j] = False
        return words


def word_search(grid_chars, dictionary):
    """
    Given a grid of letters and a dictionary, it returns all the words from the dictionary 
    that can be formed in the grid (without repetition)
    :param grid_chars: [2D array of chars]
    :param dictionary: [class Dictionary] which has methods 'is_word' & 'is_prefix'
    :return: set of words from dictionary, found by traversing grid
    """
    words = set()
    grid = WordSearch(grid_chars, dictionary)
    visited = [[False for _ in range(grid.n_columns)] for _ in range(grid.n_rows)]
    for i in range(grid.n_rows):
        for j in range(grid.n_columns):
            words.update(grid.words_starting_at(i, j, visited))
    return words
