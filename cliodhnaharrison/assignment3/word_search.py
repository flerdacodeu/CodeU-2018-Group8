#Using Python 3

#Assumes grid is uniform (same number of characters in each row/column)
#Grid can be square or rectangular

class WordSearch:

    def __init__(self, grid):
        """
        Initialises word search grid and gets the number of rows and columns.

        Arguments:
            letters: A 2D array that represents the word search grid.
        """

        self.num_rows = len(grid)
        self.num_cols = len(grid[0])
        self.grid = grid


class Dictionary:

    def __init__(self, words):
        """
        Initialises dictionary.

        Arguments:
            words: A list of words in the dictionary
        """

        self.words = words


    def is_prefix(self, check_prefix):
        """
        Returns whether the given string is a valid prefix of at least one word in the dictionary.

        Arguments:
            check_prefix: A string to be checked.

        Returns:
            True if prefix is valid, False if not
        """

        length = len(check_prefix)

        for word in self.words:
            if word[0:length] == check_prefix:
                return True
        return False


    def is_word(self, check_word):
        """
        Returns whether the given string is a valid word.

        Arguments:
            check_word: A string to be checked.

        Returns:
            True if word is present in dictionary, False if not
        """

        return check_word in words


def find_words(word_search, dictionary):
    """
    A function to find all valid words in a word search.

    Arguments:
        word_search: A WordSearch class as defined above on line 6.
        dictionary: A Dictionary class as defined above on line 23.
    """

    results = []

    for i in len(word_search.grid):
        for j in word_search.grid[i]:
            cont = True
            check_string = word_search.grid[i][j]
            while cont:
                neighbours = find_valid_neighbours(word_search, i, j)
                for cell_value in neighbours:
                    new_string = check_string + cell_value
                    if word_search.is_word(new_string):
                        results.append(new_string)
                    if word_search.is_prefix(new_string):
                        #Recursion needs to come in here I think
                        



def find_valid_neighbours(grid, row, col):
    """
    Function to find all existing adjacent cells to a certain cell.

    Arguments:
        grid: The grid containing the coordinates and the cells we are searching through.
        row: The row that the cell we are looking from is in.
        col: The column that the cell we are looking from is in.

    Returns:
        neighbours: A list of the values in all existing adjacent cells to a given cell.
    """
    neighbours = []

    row_above = row-1 >= 0
    row_below = row+1 < self.num_rows
    col_behind = col-1 >= 0
    col_ahead = col+1 < self.num_cols

    if row_above:
        neighbours.append(grid[row-1][col])
        if col_behind:
            neighbours.append(grid[row-1][col-1])
        if col_ahead:
            neighbours.append(grid[row-1][col+1])

    if row_below:
        neighbours.append(grid[row+1][col])
        if col_behind:
            neighbours.append(grid[row+1][col-1])
        if col_ahead:
            neighbours.append(grid[row+1][col+1])

    if col_ahead:
        neighbours.append(grid[row][col+1])

    if col_behind:
        neighbours.append(grid[row][col-1])

    return neighbours











test_word_search = WordSearch("AARTCD", 2, 3)
print (test_word_search.grid)
