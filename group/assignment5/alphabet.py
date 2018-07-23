# python 3
from graph import Graph
from collections import defaultdict

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
        which letter precedes another one, and represents it as a directed edge.
        A directed edge u -> v indicates that u precedes v.
        :param dictionary: [list] list of strings
        :return: [Graph] see class defined in graph.py
        """
        graph = Graph()
        for i, word1 in enumerate(dictionary):
            words = dictionary[i + 1:]
            for index in range(0, len(word1)):
                next_index_words = []
                for word2 in words:
                    if word1[index] == word2[index]:
                        next_index_words.append(word2)
                    else:
                        graph.add_edge(word1[index], word2[index])  # does not add duplicates
                if len(next_index_words) == 0:
                    break
                words = next_index_words
        return graph

    def get(self):
        """
        Finds one possible alphabet for the given dictionary.
        :return: [list of chars] ordered list of characters
        """
        return self.graph.topological_sort()

    def get_all(self):
        """
        Finds all the possible alphabets.
        :return: [list of lists of chars] where each list of chars is possible alphabet
        """
        return self.graph.all_topological_sorts()

    @staticmethod
    def sort_edges(cycles):
        """
        For each edge it counts how many times it appears in all of the cycles.
        :param cycles: [list of list] list of cycles, where a cycle is list of nodes
        :return: [dict] of <str, list> where the former is an edge represented by
         concatenating the two nodes it consists of, and the latter is the list of
         indices of all the cycles it appears in.
        """
        _edges = defaultdict(list)
        for i, cycle in enumerate(cycles):
            for j in range(1, len(cycle)):
                _edges[cycle[j-1] + '->' + cycle[j]].append(i)
        return _edges

    def inconsistent(self):
        """
        Identifies inconsistent dictionaries.
        A dictionary is inconsistent if it contains contradictory implications.
        If the dictionary is inconsistent, it returns a minimal set of constraints on 
        the alphabet that cannot be satisfied, or otherwise an empty set of constraints.
        :return: 
        """
        if not self.graph.is_cyclic():
            return []
        cycles = self.graph.all_cycles()
        selected = []
        while len(cycles) > 0:
            _edges = self.sort_edges(cycles)
            selected.append(sorted(_edges, key=lambda k: len(_edges[k]), reverse=True)[0])
            # delete cycles in which the selected edge appears
            for index in reversed(_edges[selected[-1]]):
                cycles.pop(index)
        return selected



