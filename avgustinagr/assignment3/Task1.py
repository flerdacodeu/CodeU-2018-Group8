dictionary = ["CAR", "CARD", "CART", "CAT"];
grid = ["AAR", "TCD"]
#dictionary = ["ATA"]
#grid = ["AT"]
found = []


def is_prefix(substr):
    """Checks if substr is a prefix of any of the words in the dictionary.
    (Is case sensitive.)

    :param substr: the substring to be checked
    :return: True if it is a prefix of a word in the dictionary, False if not
    """
    substr = ''.join(substr)
    for word in dictionary:
        if substr in word[:len(substr)]:
            return True
    return False


def is_word(word2):
    """Checks if word2 is a word from the dictionary.
    (Is case sensitive.)

    :param word2: the substring to be checked
    :return: True if it is a word in the dictionary, False if not

    """
    for word in dictionary:
        word2 = ''.join(word2)
        if word == word2:
            return True
    return False


def get_neighbours(x, y):
    """ Returns an array of all the neighbours of an element in the grid.

    :param x: the row of the element
    :param y: the column of the element
    :return: array containing its neighbours
    """
    possible = [1] * 8   # Will be used as flag for where there are and are not any neighbours
    """
        0 | 1 | 2
        ---------
        3 |   | 4
        ---------
        5 | 6 | 7
    """
    if x == 0:
        possible[0:3] = [0, 0, 0]
    if y == 0:
        possible[0] = 0
        possible[3] = 0
        possible[5] = 0
    if x == (len(grid) - 1):
        possible[5:8] = [0, 0, 0]
    if y == (len(grid[0]) - 1):
        possible[2] = 0
        possible[4] = 0
        possible[7] = 0

    neighbours = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y),
                  (x + 1, y + 1)]                # indexes of all possible neighbours
    for i in range(0, len(possible)):            # sets the values of non-existent neighbours to 0
        if not possible[i]:
            neighbours[i] = 0

    neighbours.sort()

    for i in range(len(neighbours)):            # removes all 0 elements to keep only the neighbours, which exist
        if neighbours[i] != 0:
            neighbours = neighbours[i:]
            break
    return neighbours


def find_neighbours_of_all():
    """ Creates a dictionary with:
    key: tuple of the element in the grid
    value: an array of all its neighbours

    :return: dictionary of all the tuples and their neighbours
    """
    all_n = {}
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            all_n[(i, j)] = get_neighbours(i, j)
    return all_n


def _find_word_from(x, y, path_tuples, path):
    """ Helper function for find_words. Finds all the words from dictionary that can be formed starting at the element
    with coordinates (x, y) on the grid and appends them to the global variable found.
    Uses depth first search without keeping a list of the visited nodes so that we can traverse through them again in
    search of new words. (only checks if the next node we want to use is not already a part of the word we have formed
    so far)

    :param x: the row of the element
    :param y: the column of the element
    :param path_tuples: keeps the coordinates of the elements used for the current word (the path) as tuples
    :param path: an array of the actual letters in the word so far.
    """
    path_tuples.append((x, y))
    path.append(grid[x][y])
    if not is_prefix(path):
        path.pop()
        path_tuples.pop()
        return
    if is_word(path) and ''.join(path) not in found:

        found.append(''.join(path))

    for neighbour in all_neighbours[(x, y)]:
        if neighbour not in path_tuples:
            _find_word_from(neighbour[0], neighbour[1], path_tuples, path)
    path.pop()
    path_tuples.pop()


def find_words(x, y):
    """Main function used to find all words that can be found in the dictionary that can be formed starting at the
    element with coordinates (x, y).

    :param x: row of the element
    :param y: column of the element
    """
    if x > len(grid)-1 or x < 0 or y > len(grid[0]) or y < 0:
        print "Element out of range"
        return False
    path_tuples = []
    path = []

    return _find_word_from(x, y, path_tuples, path)


def main():
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            find_words(i, j)


all_neighbours = find_neighbours_of_all()
