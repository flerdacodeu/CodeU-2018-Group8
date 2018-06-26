found = []

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
    for i in range (0, len(grid[0])):
        if (x == -1 or x == len(grid)) and y == i:
            return False
    for j in range (-1, len(grid)+1):
        if x == j and (y == -1 or y == len(grid[0])):
            return False
    return True

def get_neighbours(x, y, grid):
    """ Returns an array of all the neighbours of an element in the grid.

    :param x: the row of the element
    :param y: the column of the element
    :param grid: a list of lists: the grid in which the function is looking for words
    :return: array containing its neighbours
    """

    neighbours = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y),
                  (x + 1, y + 1)]                # indexes of all possible neighbours

    for i in range(len(neighbours)):
        if not is_valid(neighbours[i][0], neighbours[i][1], grid):
            neighbours[i] = 0

    neighbours.sort()

    for i in range(len(neighbours)):            # removes all 0 elements to keep only the neighbours, which exist
        if neighbours[i] != 0:
            neighbours = neighbours[i:]
            break
    return neighbours


def find_neighbours_of_all(grid):
    """ Creates a dictionary with:
    key: tuple of the element in the grid
    value: an array of all its neighbours

    :param grid: a list of lists: the grid in which the function is looking for words
    :return: dictionary of all the tuples and their neighbours
    """
    all_n = {}
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            all_n[(i, j)] = get_neighbours(i, j, grid)
    return all_n


def _find_word_from(x, y, path_tuples, path, grid, dictionary):
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
    """
    path_tuples.append((x, y))
    path.append(grid[x][y])
    if not is_prefix(path, dictionary):
        path.pop()
        path_tuples.pop()
        return
    if is_word(path, dictionary) and ''.join(path) not in found:

        found.append(''.join(path))

    for neighbour in all_neighbours[(x, y)]:
        if neighbour not in path_tuples:
            _find_word_from(neighbour[0], neighbour[1], path_tuples, path, grid, dictionary)
    path.pop()
    path_tuples.pop()


def find_words(x, y, grid, dictionary):
    """Main function used to find all words that can be found in the dictionary that can be formed starting at the
    element with coordinates (x, y).
    :param x: row of the element
    :param y: column of the element
    :param grid: a list of lists: the grid in which the function is looking for words
    :param dictionary: a list of words: the dictionary with the words to which the function is comparing substr
    """
    if x > len(grid)-1 or x < 0 or y > len(grid[0]) or y < 0:
        print "Element out of range"
        return False
    path_tuples = []
    path = []

    return _find_word_from(x, y, path_tuples, path, grid, dictionary)


def main(grid, dictionary):
    """

    :param grid: a list of lists: the grid in which the function is looking for words
    :param dictionary: a list of words: the dictionary with the words to which the function is comparing substr
    :return:
    """
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            find_words(i, j, grid, dictionary)
