def is_prefix(substr, dictionary):
    """Checks if substr is a prefix of any of the words in the dictionary.
    (Is case sensitive.)
    :param substr: the substring to be checked
    :param dictionary: a list of words: the dictionary with the words to which the function is comparing substr
    :return: True if it is a prefix of a word in the dictionary, False if not
    """
    substr = ''.join(substr)
    for word in dictionary:
        if substr in word[:len(substr)]:
            return True
    return False


def is_word(word2, dictionary):
    """Checks if word2 is a word from the dictionary.
    (Is case sensitive.)
    :param word2: the substring to be checked
    :param dictionary: a list of words: the dictionary with the words to which the function is comparing substr
    :return: True if it is a word in the dictionary, False if not
    """
    for word in dictionary:
        word2 = ''.join(word2)
        if word == word2:
            return True
    return False

def is_valid(x, y, grid):
    """ Checks whether a tile with coordinates x ( row), y (column) exists in the grid.

    :param x: the row of the element
    :param y: the column of the element
    :param grid: a list of lists: the grid in which the function is looking for words
    :return: True if the tile exists on the grid, False if not
    """
    return (x >= 0) and (x < len(grid)) and (y >= 0) and (y < len(grid[0]))

# found = []

def _find_word_from(x, y, path_tuples, path, grid, dictionary, found):
    """ Helper function for find_words. Finds all the words from dictionary that can be formed starting at the element
    with coordinates (x, y) on the grid and appends them to the global variable found.
    Uses depth first search without keeping a list of the visited nodes so that we can traverse through them again in
    search of new words. (only checks if the next node we want to use is not already a part of the word we have formed
    so far)
    :param x: the row of the element
    :param y: the column of the element
    :param path_tuples: keeps the coordinates of the elements used for the current word (the path) as tuples
    :param path: an array of the actual letters in the word so far.
    :param grid: a list of lists: the grid in which the function is looking for words
    :param dictionary: a list of words: the dictionary with the words to which the function is comparing substr
    :param found: a list that holds the words, which have been found so far (is being kept
    so that the function does not print duplicates)
    """
    path_tuples.append((x, y))
    path.append(grid[x][y])
    if not is_prefix(path, dictionary):
        path.pop()
        path_tuples.pop()
        return
    if is_word(path, dictionary) and ''.join(path) not in found:
        found.append(''.join(path))

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if is_valid(i, j, grid) and (i, j) not in path_tuples:
                _find_word_from(i, j, path_tuples, path, grid, dictionary, found)
    path.pop()
    path_tuples.pop()


def find_words(grid, dictionary):
    """ Goes through all of the tiles, and finds every new word (beginning with that tile) that can be found.

    :param grid: a list of lists: the grid in which the function is looking for words
    :param dictionary: a list of words: the dictionary with the words to which the function is comparing substr
    :return: a list oontaining the unique words from the dictionary, which have been found in the grid
    """
    found = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            path_tuples = []
            path = []
            _find_word_from(i, j, path_tuples, path, grid, dictionary, found)
    return found
