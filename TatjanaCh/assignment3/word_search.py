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


def wordsStartingAt(grid, dictionary, i, j, sub_word='', _visited=None):
    """
    Given a grid of letters and a dictionary, it returns all the words from the dictionary 
    that can be formed starting from char (i, j) in the grid (without repetition)
    :param grid: [ 2D array of chars]
    :param dictionary: [class Dictionary] which has methods 'isWord' & 'isPrefix'
    :param i: [int]
    :param j: [int]
    :param sub_word: [ str ]
    :param _visited: [ 2D array of bool] 
    :return: [set]  of words
    """
    if _visited is None:
        visited = [[False for ii in range(len(grid[i]))] for jj in range(len(grid))]
    else:
        visited = [[False if _visited[ii][jj] is False else True for jj in range(len(grid[i]))] for ii in range(len(grid))]
    words = set()
    sub_word += grid[i][j]
    visited[i][j] = True

    if dictionary.isWord(sub_word):
        words.add(sub_word)

    if dictionary.isPrefix(sub_word):
        for ii in range(max(i - 1, 0), min(i + 2, len(grid))):
            for jj in range(max(j - 1, 0), min(j + 2, len(grid[ii]))):
                if not visited[ii][jj] and dictionary.isPrefix(sub_word + grid[ii][jj]):
                    words.update(wordsStartingAt(grid, dictionary, i=ii, j=jj,
                                                 sub_word=sub_word[:],
                                                 _visited=visited))
    return words


def wordSearch(grid, dictionary):
    """
    Given a grid of letters and a dictionary, it returns all the words from the dictionary 
    that can be formed in the grid (without repetition)
    :param grid: [2D array of chars]
    :param dictionary: [class Dictionary] which has methods 'isWord' & 'isPrefix'
    :return: set of words from dictionary, found by traversing grid
    """
    words = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            words.update(wordsStartingAt(grid, dictionary, i, j))
    return words
