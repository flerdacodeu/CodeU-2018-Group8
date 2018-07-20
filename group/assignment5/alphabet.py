# python 3
from graph import Graph


class Alphabet:
    """
    Given a dictionary of words  (a list of words in lexicographic order), 
    it infers the alphabet (ordered list of characters) that is consistent 
    with the given dictionary.
    """

    def __init__(self, dictionary):
        self.graph = self.edges(dictionary)

    @staticmethod
    def edges(dictionary):
        """
        Given an ordered dictionary of words, it extracts information regarding
        which letter precedes another one, and represents it as directed edge.
        :param dictionary: [list] list of strings
        :return: 
        """
        G = Graph()
        for i, word1 in enumerate(dictionary):
            words = dictionary[i + 1:]
            for index in range(0, len(word1)):
                next_index_words = []
                for word2 in words:
                    if word1[index] == word2[index]:
                        next_index_words.append(word2)
                    else:
                        G.add_edge(word1[index], word2[index])  # does not add duplicates
                if len(next_index_words) == 0:
                    break
                words = next_index_words
        return G

    def get(self):
        return self.graph.topological_sort()
