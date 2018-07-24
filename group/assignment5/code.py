# -*- coding: utf-8 -*-
from copy import deepcopy
from typing import List, Dict, Set, Generator

"""Computes an alphabet given a dictionary of all words in a language.

Main problem: returns any alphabet.
Challenge #1: returns all possible alphabets.  
"""


# main problem
def get_alphabet(dictionary: List[str]) -> List[str]:
    """Extracts an alphabet from a given dictionary of words.

    Args:
        dictionary: A lexicographically ordered list of all words in a language.

    Returns:
        An alphabet, an ordered list of characters.

    Raises:
        ValueError: No alphabet is consistent.
    """
    graph = _build_graph(dictionary)
    starting_nodes = [node for node, edges in graph.items()
                      if not edges["incoming"]]
    alphabet = []
    while starting_nodes:
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


# challenge1
def get_all_alphabets(dictionary: List[str]) -> List[List[str]]:
    """Extracts all possible alphabets from a given dictionary of words.

    Args:
        dictionary: A lexicographically ordered list of all words in a language.

    Returns:
        A list of all valid alphabets.

    Raises:
        ValueError: No alphabet is consistent.
    """

    def _brute_force(starting_nodes: List[str],
                     graph: Dict[str, Dict[str, Set[str]]],
                     alphabet: List[str]) -> Generator[List[str], None, None]:
        """Finds all possible topological sorts for a given directed graph.

        Args:
            starting_nodes: Nodes without incoming edges.
            graph: A directed graph of characters, a dictionary with two values,
            "incoming" (contains all the characters that have incoming edges to
            a character) and "outgoing" (all the characters that have outgoing
            edges from the current character).
            alphabet: A list of characters that have already been sorted.

        Yields:
            An alphabet, an ordered list of characters.

        Raises:
            ValueError: No alphabet is consistent.
        """
        for curr_node in starting_nodes:
            tmp_graph = deepcopy(graph)
            tmp_starting_nodes = starting_nodes.copy()
            tmp_starting_nodes.remove(curr_node)
            alphabet.append(curr_node)
            for node in tmp_graph[curr_node]["outgoing"].copy():
                tmp_graph[curr_node]["outgoing"].remove(node)
                tmp_graph[node]["incoming"].remove(curr_node)
                if not tmp_graph[node]["incoming"]:
                    tmp_starting_nodes.append(node)
            yield from _brute_force(tmp_starting_nodes, tmp_graph, alphabet)
            alphabet.pop()
        if not starting_nodes:
            yield alphabet.copy()
            for node in graph:
                if graph[node]["incoming"] or graph[node]["outgoing"]:
                    raise ValueError("Dictionary is inconsistent!")

    main_graph = _build_graph(dictionary)
    main_starting_nodes = [node for node, edges in main_graph.items()
                           if not edges["incoming"]]
    return list(_brute_force(main_starting_nodes, main_graph, []))


def _build_graph(dictionary: List[str]) -> Dict[str, Dict[str, Set[str]]]:
    """Builds a directed graph of characters from a dictionary of words.

    For example, if the letter "k" precedes the letter "b" in the dictionary,
    the graph will contain a directed edge k->b.

    Args:
        dictionary: A lexicographically ordered list of all words in a language.

    Returns: A dictionary with two values, "incoming" (contains all the chars
        that have incoming edges to the current character) and "outgoing"
        (contains all the characters that have outgoing edges from the current
        character).
    """
    characters = {character for word in dictionary for character in word}
    graph = {char: {"outgoing": set(), "incoming": set()}
             for char in characters}
    for i in range(0, len(dictionary) - 1):
        for c1, c2 in zip(dictionary[i], dictionary[i + 1]):
            if c1 != c2:
                graph[c1]["outgoing"].add(c2)
                graph[c2]["incoming"].add(c1)
                break
    return graph
