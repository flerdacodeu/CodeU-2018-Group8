# -*- coding: utf-8 -*-
import unittest

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
    level = 0
    graph = {}
    change = True

    while(change):
        change = False
        curr_letter = ""
        curr_prefix = ""
        for word in dictionary:
            if level < len(word):
                change = True
                if word[level] not in graph:
                    graph[word[level]] = {"outgoing":set(), "incoming":set()}
                if word[level] != curr_letter and word[:level] == curr_prefix:
                    if curr_letter:
                        if curr_letter not in graph:
                            graph[curr_letter] = {"outgoing":set(), "incoming":set()}
                        graph[curr_letter]["outgoing"].add(word[level])
                        graph[word[level]]["incoming"].add(curr_letter)
                curr_letter = word[level]
                curr_prefix = word[:level]
        level += 1
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

if __name__ == "__main__":
    unittest.main()