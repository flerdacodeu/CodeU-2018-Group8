import logging
#logging.basicConfig(filename="code.log", filemode='w', level=logging.DEBUG)

class Grid():
    """
    Grid of letters: array of strings
    """

    def __init__(self, table):
        self.grid = table
        self.rows = 0
        self.cols = 0
        if table is not None:
            self.rows = len(table)
            self.cols = len(table[0])

    def get_adjacent_cells(self, x0, y0):
        """
        Return all adjacent cells.
        :param x0, y0: initial coords.
        :return: list of dict, each dict contains keys 'letter' and 'coords'.
        """
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        adjacent_cells = []
        for i in range(8):
            x_new = x0 + dx[i]
            y_new = y0 + dy[i]
            if 0 <= x_new < self.rows and 0 <= y_new < self.cols:
                adjacent_cells.append({'coords': (x_new, y_new), 'letter': self.grid[x_new][y_new]})
        return adjacent_cells

    def get_letter(self, x0, y0):
        """
        Get letter from grid.
        :param x0, y0: initial coords.
        :return: char.
        """
        return self.grid[x0][y0]


class Dictionary():
    """
    Using Trie data structure.
    ---
    Example of trie structure for [CAR, CARD, CART, CAT].
    {C :
      {A :
        {R :
          {D :
            {END!}}
          {T :
            {END!}}
          {END!}}
        {T :
          {END!}}}}
    """
    def __init__(self, words=None, use_cache=False):
        """
        :param words: initial words, list of strings.
        :param use_cache: use "cache memory" to avoid recomputation of the same values.
        When use_cache is True methods is_word and is_prefix should not receive a string.
            Results of these methods depends only on cache_root.
            It is necessary use navigation cash methods: init, add, del.
        """
        self.root = dict()
        self.use_cache = use_cache
        if self.use_cache:
            self.init_cache()
        if not words:
            return
        for word in words:
            current_root = self.root
            for letter in word:
                current_root.setdefault(letter, {})
                current_root[letter]['__previous__'] = current_root
                current_root = current_root[letter]
            current_root['__end__'] = '__end__'
        self.debug_trie(self.root)

    def is_word(self, word=''):
        """
        Returns whether the given string is a valid word.
        :param word: required parameter if use_cache is False
        :return: bool
        """
        if self.use_cache:
            if self.cache_additional_len == 0 and '__end__' in self.cache_root:
                return True
            else:
                return False
        current_root = self.root
        for letter in word:
            if current_root:
                current_root = current_root.get(letter)
        if current_root and '__end__' in current_root:
            return True
        return False

    def is_prefix(self, prefix=''):
        """
        Returns whether the given string is a prefix of at least one word in thedictionary.
        :param prefix: required parameter if use_cache is False
        :return: bool
        """
        if self.use_cache:
            if self.cache_additional_len:
                return False
            else:
                return True
        current_root = self.root
        for letter in prefix:
            if current_root:
                current_root = current_root.get(letter)
            else:
                return False
        if current_root:
            return True
        else:
            return False

    def init_cache(self):
        """
        Save root of trie to cache root.
        :return: None
        """
        self.cache_root = self.root
        self.cache_additional_len = 0

    def add_letter_cache(self, letter):
        """
        Change cache root. Step to descendant of the cache node.
        :return: None
        """
        logging.debug("ADD " + letter)
        if letter in self.cache_root:
            self.cache_root = self.cache_root[letter]
        else:
            self.cache_additional_len += 1

    def del_letter_cache(self):
        """
        Change cache root. Step to ancestor of the cache node.
        :return: None
        """
        logging.debug("DEL")
        if self.cache_additional_len:
            self.cache_additional_len -= 1
        else:
            self.cache_root = self.cache_root.get('__previous__')

    def debug_trie(self, root=None, tabs=0):
        """
        Print dict to log file in useful format.
        :param root:
        :param tabs: count of nested nodes
        :return: None
        """
        if root == None:
            root = self.root
        for letter in sorted(root.keys()):
            if letter == "__previous__":
                continue
            if letter == "__end__" :
                logging.debug(" "*4*tabs + "{END!}")
                return
            logging.debug(" "*4*tabs + "{" + letter + " : ")
            self.debug_trie(root[letter], tabs + 1)
            logging.debug(" "*4*tabs + "}")
        return

def word_search(grid, dictionary):
    """
    Find all the words from the dictionary that can be formed in the grid.
    :param grid: grid of letters
    :param dictionary: use_cache should be True
    :return: set of all words found
    """
    set_all_words = set()
    def dfs(cell0, current_word):
        """
        Add to result set all words which started in current cell.
        :param cell0: current node of trie.
        :param current_word: current prefix in the grid.
        :return: None
        """
        logging.debug("**DFS")
        logging.debug(cell0)
        x0, y0 = cell0['coords']
        letter0 = cell0['letter']
        dictionary.add_letter_cache(letter0)
        if not dictionary.is_prefix():
            dictionary.del_letter_cache()
            logging.debug(current_word + letter0 + " is not prefix")
            return
        if dictionary.is_word():
            set_all_words.add(current_word+letter0)
        used.add((x0, y0))
        for cell in grid.get_adjacent_cells(x0, y0):
            if not cell['coords'] in used:
                dfs(cell, current_word+letter0)
        used.remove((x0, y0))
        dictionary.del_letter_cache()

    for i in range(grid.rows):
        for j in range(grid.cols):
            used = set()
            dictionary.init_cache()
            cell = {'coords': (i, j), 'letter': grid.get_letter(i, j)}
            dfs(cell, '')
    logging.debug(set_all_words)
    return set_all_words
