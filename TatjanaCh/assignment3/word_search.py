# Python 3
from abc import ABCMeta, abstractmethod


class Dictionary(metaclass=ABCMeta):
    """
    Abstract Base Class, forcing derived classes to implement 'isWord' & 'isPrefix'
    """

    @abstractmethod
    def isWord(self, _str):
        pass

    @abstractmethod
    def isPrefix(self, _str):
        pass


class WordSearch():
    def __init__(self, grid, dictionary):
        """
        
        :param grid: [2D array of chars]
        :param dictionary: [class Dictionary] which has methods 'isWord' & 'isPrefix'
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

    def neighbors(self, i, j, visited):
        """
        A generator that yields neighbors which are not visited
        :param i: [int]
        :param j: [int]
        :param visited: [ 2D array of bool]
        :return: [tuple of integers] which correspond to row, column 
        """
        for ii in range(max(i - 1, 0), min(i + 2, self.n_rows)):
            for jj in range(max(j - 1, 0), min(j + 2, self.n_columns)):
                if not visited[ii][jj]:
                    yield ii, jj


def wordsStartingAt(grid, i, j, visited, sub_word=''):
    """
    Given a grid of letters and a dictionary, it returns all the words from the dictionary 
    that can be formed starting from char (i, j) in the grid (without repetition)
    :param grid: [class WordSearch] see above
    :param i: [int]
    :param j: [int]
    :param sub_word: [ str ]
    :param visited: [ 2D array of bool] True and False denote visited and not visited letter, respectively
    :return: [set]  of words
    """
    words = set()
    sub_word += grid[i, j]
    visited[i][j] = True

    if grid.dictionary.isWord(sub_word):
        words.add(sub_word)

    if grid.dictionary.isPrefix(sub_word):
        for ii, jj in grid.neighbors(i, j, visited):
            words.update(wordsStartingAt(grid, i=ii, j=jj, visited=visited, sub_word=sub_word[:]))
    visited[i][j] = False
    return words


def wordSearch(grid_chars, dictionary):
    """
    Given a grid of letters and a dictionary, it returns all the words from the dictionary 
    that can be formed in the grid (without repetition)
    :param grid_chars: [2D array of chars]
    :param dictionary: [class Dictionary] which has methods 'isWord' & 'isPrefix'
    :return: set of words from dictionary, found by traversing grid
    """
    words = set()
    grid = WordSearch(grid_chars, dictionary)
    visited = [[False for _ in range(grid.n_columns)] for _ in range(grid.n_rows)]
    for i in range(grid.n_rows):
        for j in range(grid.n_columns):
            words.update(wordsStartingAt(grid, i, j, visited))
    return words
