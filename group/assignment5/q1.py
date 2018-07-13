# -*- coding: utf-8 -*-
import unittest
from copy import deepcopy

def build_graph(dictionary):
    """
    Builds a directed graph of characters from a 
    lexicographically ordered dictionary of words.
    For example, if the letter "k" precedes the
    letter "b" in the dictionary, the graph will 
    contain a directed edge k->b.
        - dictionary: list of strings, all the
                      words in the dictionary
        Returns:
            - graph: dictionary with two values,
            "incoming" (contains all the 
            characters that have incoming edges
            to the current character) and 
            "outgoing" (contains all the 
            characters that have outgoing edges
            from the current character)
    """
    characters = set()
    for word in dictionary:
        characters = characters.union(word)
    graph = {char : {"outgoing":set(), "incoming":set()} for char in characters}
    for i in range(0, len(dictionary) - 1):
        for c1, c2 in zip(dictionary[i], dictionary[i+1]):
            if c1 != c2:
                graph[c1]["outgoing"].add(c2)
                graph[c2]["incoming"].add(c1)
                break
    return graph

def unknown_alphabet(dictionary):
    """
    Extracts an alphabet (ordered list of characters)
    from a lexicographically ordered dictionary of words.
        - dictionary: list of strings, all the
                      words in the dictionary
        Returns:
            - alphabet: list of strings, an ordered
                        list of characters
    """
    dictionary = map(lambda x: x.decode("utf8"), dictionary)
    graph = build_graph(dictionary)
    starting_nodes = [node for node, edges in graph.items() if not edges["incoming"]]

    alphabet = []
    while(starting_nodes):
        curr_node = starting_nodes.pop()
        alphabet.append(curr_node)
        for node in graph[curr_node]["outgoing"].copy():
            graph[curr_node]["outgoing"].remove(node)
            graph[node]["incoming"].remove(curr_node)
            if not graph[node]["incoming"]:
                starting_nodes.append(node)
    for node in graph:
        if graph[node]["incoming"] or graph[node]["outgoing"]:
            raise ValueError("Dictionary is inconsistent!")
    return alphabet


#challenge1
def all_alphabets(dictionary):
    """
        Extracts all possible alphabets (ordered list of characters)
        from a lexicographically ordered dictionary of words.
            - dictionary: list of strings, all the
                          words in the dictionary
            Returns:
                - all_alphabets: list of ordered alphabets list of strings
        """
    def _brute_force(starting_nodes, graph):
        for curr_node in starting_nodes:
            tmp_graph = deepcopy(graph)
            tmp_starting_nodes = deepcopy(starting_nodes)
            tmp_starting_nodes.remove(curr_node)
            alphabet.append(curr_node)
            for node in tmp_graph[curr_node]["outgoing"].copy():
                tmp_graph[curr_node]["outgoing"].remove(node)
                tmp_graph[node]["incoming"].remove(curr_node)
                if not tmp_graph[node]["incoming"]:
                    tmp_starting_nodes.append(node)
            _brute_force(tmp_starting_nodes, tmp_graph)
            alphabet.pop()
        if not starting_nodes:
            result_alphabets.append(deepcopy(alphabet))
            for node in graph:
                if graph[node]["incoming"] or graph[node]["outgoing"]:
                    raise ValueError("Dictionary is inconsistent!")

    dictionary = map(lambda x: x.decode("utf8"), dictionary)
    graph = build_graph(dictionary)
    starting_nodes = [node for node, edges in graph.items() if not edges["incoming"]]
    alphabet = []
    result_alphabets = []
    _brute_force(starting_nodes, graph)
    return result_alphabets

class AlphabetTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(unknown_alphabet([]), [])

    def test_empty_string(self):
        self.assertEqual(unknown_alphabet([""]), [])

    def test_one_word(self):
        self.assertEqual(unknown_alphabet(["abc"]), ["b", "c", "a"])

    def test_base_example(self):
        self.assertEqual(unknown_alphabet(["art", "rat", "cat", "car"]), ["t", "a", "r", "c"])

    def test_more_complicated_example(self):
        self.assertEqual(unknown_alphabet(["alp", "art", "arm", "rat", "cat", "car"]),
                                           ["t", "m", "p", "l", "a", "r", "c"])

    def test_cycle_raises_valueerror(self):
        self.assertRaises(ValueError, unknown_alphabet, ["art", "rat", "cat", "car", "rr", "ra"])

    def test_nonascii_chars(self):
        self.assertEqual(unknown_alphabet(["älp", "ärt", "ärm", "rat", "cat", "car"]),
                    map(lambda x: x.decode("utf8"), ["t", "m", "p", "l", "ä", "r", "c", "a"]))

class AllAlphabetTest(unittest.TestCase):
    def test_base(self):
        self.assertEqual(all_alphabets(["art", "rat", "cat", "car"]), [list('atrc'), list('tarc')])

if __name__ == "__main__":
    unittest.main()
