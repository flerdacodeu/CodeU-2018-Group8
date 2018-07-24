# -*- coding: utf-8 -*-
from copy import deepcopy


# main problem
def _build_graph(dictionary):
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
    graph = {char: {"outgoing": set(), "incoming": set()}
             for char in characters}
    for i in range(0, len(dictionary) - 1):
        for c1, c2 in zip(dictionary[i], dictionary[i + 1]):
            if c1 != c2:
                graph[c1]["outgoing"].add(c2)
                graph[c2]["incoming"].add(c1)
                break
    return graph


def get_alphabet(dictionary):
    """
    Extracts an alphabet (ordered list of characters)
    from a lexicographically ordered dictionary of words.
        - dictionary: list of strings, all the
                      words in the dictionary
        Returns:
            - alphabet: list of strings, an ordered
                        list of characters
    """
    graph = _build_graph(dictionary)
    starting_nodes = [node for node, edges in graph.items() if not edges["incoming"]]

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
def get_all_alphabets(dictionary):
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
            tmp_starting_nodes = starting_nodes.copy()
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
            yield alphabet.copy()
            for node in graph:
                if graph[node]["incoming"] or graph[node]["outgoing"]:
                    raise ValueError("Dictionary is inconsistent!")

    main_graph = _build_graph(dictionary)
    main_starting_nodes = [node for node, edges in main_graph.items()
                           if not edges["incoming"]]
    alphabet = []
    return list(_brute_force(main_starting_nodes, main_graph))