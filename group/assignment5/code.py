import logging
logging.basicConfig(filename="code.log", filemode='w', level=logging.DEBUG)

class Dictionary():
    """
    Stores dictionary and build alphabet using topological sorting.
    Attributes:
        words: ordered list of words
        n: count of words
        characters: set all different characters from words
        m: count of characters
        graph: Map of lists. Vertices of the graph are characters of the alphabet.
            There is an edge from c1 to c2 if in the dictionary are two neighborhood words which require it.
            Keys of the map are characters of the alphabet.
            The list contains all characters which have key-character as an adjacent.
        used: attribute for topological sort;
            map for each key stores 0 (not used) or 1 (using now) or 2 (used).
        alphabet: ordered alphabet (store after call get_alphabet method)
    """
    def __init__(self, words):
        """
        :param words: ordered list of words
        """
        self.words = words
        self.n = len(self.words)
        self.characters = set()
        for word in self.words:
            self.characters = self.characters.union(word)
        self.m = len(self.characters)
        self._init_attributes()

    def _init_attributes(self):
        """
        Initialization attributes for topological sorting.
        """
        self.used = {char: 0 for char in self.characters}
        self.consistent_alphabet = True
        self.alphabet = []
        self.graph = {char: [] for char in self.characters}

    def _build_ordered_graph_of_characters(self):
        """
        Build the graph. Vertices of the graph are characters of the alphabet.
        There is an edge from v character to u character if in the dictionary are two neighborhood words which require it.
        :return: graph: map of lists.
        Keys of the map are characters of the alphabet.
        The list contains all characters which have key-character as an adjacent.
        """
        #no characters in dictionary
        if self.m == 0:
            return
        next_word = self.words[0]
        for i in range(1, self.n):
            prev_word = next_word
            next_word = self.words[i]
            for v, u in zip(prev_word, next_word):
                if v != u:
                    self.graph[v].append(u)
                    break

    def _topological_sort(self, v):
        """
        DFS from vertex v.
        :param v: not used character
        """
        if not self.consistent_alphabet:
            return
        self.used[v] = 1
        for u in self.graph[v]:
            if self.used[u] == 0:
                self._topological_sort(u)
            #cycle
            if self.used[u] == 1:
                self.consistent_alphabet = False
        self.alphabet.append(v)
        self.used[v] = 2

    def get_alphabet(self):
        """
        Return ordered alphabet.
        :param words: list of strings.
        :return: ordered list of characters or -1 if no alphabet is consistent.
        """
        self._init_attributes()
        self._build_ordered_graph_of_characters()
        logging.debug(self.graph)
        for c in self.characters:
            if self.used[c] == 0:
                self._topological_sort(c)
        if not self.consistent_alphabet:
            return -1
        return self.alphabet[::-1]

def get_alphabet(words):
    """
    Return ordered alphabet.
    :param words: list of strings.
    :return: ordered list of characters or -1 if no alphabet is consistent.
    """
    d = Dictionary(words)
    return d.get_alphabet()

