#Using Python 3

#Assumes grid is uniform (same number of characters in each row/column)
#Grid can be square or rectangular

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

        return check_word in self.words

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
        self.visited = [[0 for x in range(self.num_cols)] for y in range(self.num_rows)]

    def find_valid_neighbours(self, grid, row, col):
        """
        Function to find all existing adjacent cells to a certain cell.

        Arguments:
            grid: The grid containing the coordinates and the cells we are searching through.
            row: The row that the cell we are looking from is in.
            col: The column that the cell we are looking from is in.

        Returns:
            neighbours: A list of the coordinates of all existing adjacent cells to a given cell.
        """
        neighbours = []

        row_above = row-1 >= 0
        row_below = row+1 < self.num_rows
        col_behind = col-1 >= 0
        col_ahead = col+1 < self.num_cols

        if row_above:
            neighbours.append((row-1, col))
            if col_behind:
                neighbours.append((row-1, col-1))
            if col_ahead:
                neighbours.append((row-1, col+1))

        if row_below:
            neighbours.append((row+1, col))
            if col_behind:
                neighbours.append((row+1, col-1))
            if col_ahead:
                neighbours.append((row+1, col+1))

        if col_ahead:
            neighbours.append((row, col+1))

        if col_behind:
            neighbours.append((row, col-1))

        return neighbours



    def find_words(self, dictionary):
        """
        A function to find all valid words in a word search.

        Arguments:
            dictionary: A Dictionary class as defined above on line 23.

        Returns:
            results: A set of words from the dictionary found in the word search.
        """

        self.results = set()

        for row in range(0, self.num_rows):
            for col in range(0, self.num_cols):
                self._recurse("", row, col, dictionary)
        return self.results



    def _recurse(self, word, row, col, dictionary):
        """
        Recurses through neighbours of row, col if the given word is a valid prefix of a word in the dictionary.

        Arguments:
            word: A string of characters from the word search that may be a word from the dictionary.
            row: An int that represents the row of the 2D array that the cell is located.
            col: An int that represents the column of the 2D array that the cell is located.
        """
        self.visited[row][col] = 1
        word += self.grid[row][col]

        if dictionary.is_word(word):
            self.results.add(word)

        if dictionary.is_prefix(word):
            neighbours = self.find_valid_neighbours(self.grid, row, col)

            for r, c in neighbours:
                if self.visited[r][c] == 0:
                    self._recurse(word, r, c, dictionary)

        self.visited[row][col] = 0




test_word_search = WordSearch([["A", "A", "R"], ["T", "C", "D"]])
test_dictionary = Dictionary(["CAR", "CARD", "CART", "CAT"])
print (test_word_search.find_words(test_dictionary))
