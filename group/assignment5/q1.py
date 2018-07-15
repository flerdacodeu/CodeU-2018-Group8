# -*- coding: utf-8 -*-
import unittest
from copy import deepcopy

#main problem
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
    characters = {character for word in dictionary for character in word}
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
            yield from _brute_force(tmp_starting_nodes, tmp_graph)
            alphabet.pop()
        if not starting_nodes:
            yield deepcopy(alphabet)
            for node in graph:
                if graph[node]["incoming"] or graph[node]["outgoing"]:
                    raise ValueError("Dictionary is inconsistent!")

    graph = build_graph(dictionary)
    starting_nodes = [node for node, edges in graph.items() if not edges["incoming"]]
    alphabet = []
    return list(_brute_force(starting_nodes, graph))

class AlphabetTest(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(unknown_alphabet([]), [])

    def test_empty_string(self):
        self.assertEqual(unknown_alphabet([""]), [])

    def test_one_word(self):
        self.assertTrue(tuple(unknown_alphabet(["abc"])) in {tuple("abc"),
                                                             tuple("acb"),
                                                             tuple("bac"),
                                                             tuple("bca"),
                                                             tuple("cab"),
                                                             tuple("cba"),
                                                             })

    def test_base_example(self):
        self.assertTrue(tuple(unknown_alphabet(["art", "rat", "cat", "car"])) in
                        {tuple("tarc"), tuple("atrc")})

    def test_more_complicated_example(self):
        self.assertTrue(unknown_alphabet(["alp", "art", "arm", "rat", "cat", "car"]) in
                         all_alphabets(["alp", "art", "arm", "rat", "cat", "car"]))

    def test_cycle_raises_valueerror(self):
        self.assertRaises(ValueError, unknown_alphabet, ["art", "rat", "cat", "car", "rr", "ra"])

    def test_nonascii_chars(self):
        self.assertCountEqual(unknown_alphabet(["älp", "ärt", "ärm", "rat", "cat", "car"]),
                    map(lambda x: x, ["t", "m", "p", "l", "ä", "r", "c", "a"]))

class AllAlphabetTest(unittest.TestCase):
    def test_all_alphabets_base(self):
        self.assertCountEqual(all_alphabets(["art", "rat", "cat", "car"]), [list('atrc'), list('tarc')])

if __name__ == "__main__":
    unittest.main()
