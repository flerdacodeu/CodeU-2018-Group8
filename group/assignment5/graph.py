# python 3
from collections import defaultdict


class Graph:
    """
    Implements Graph, where the edges are stored separately per node.
    """

    def __init__(self):
        self.graph = defaultdict(list)  # dict containing adjacency lists per node

    def add_edge(self, u, v):
        """
        If non-existing, it adds an edge: u->v, and it inserts v as a node.
        :param u: [int/char] node
        :param v: [int/char] node
        :return: None
        """
        if not (self.graph[u] and v in self.graph[u]):
            self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v]

    def dfs_util(self, v, visited, queue):
        """
        Recursive function. Used by dfs().
        :param v: [int/char] current node
        :param visited: [dict] whose values are boolean
        :param queue: [list] where the result is appended
        :return: None
        """
        visited[v] = True
        queue.append(v)

        for u in self.graph[v]:
            if not visited[u]:
                self.dfs_util(u, visited, queue)

    def dfs(self):
        """
        Depth first search. Uses the recursive function dfs_util.
        :return: [list] of nodes (int/char)
        """
        visited = dict.fromkeys(self.graph, False)
        queue = []

        for v in self.graph:
            if not visited[v]:
                self.dfs_util(v, visited, queue)
        return queue

    def topological_sort_util(self, v, visited, stack):
        """
        Recursive function. Used by topological_sort().
        :param v: [int/char] current node
        :param visited: [dict] whose values are boolean
        :param stack: [list] where the result is pushed
        :return: None
        """
        visited[v] = True
        for u in self.graph[v]:
            if not visited[u]:
                self.topological_sort_util(u, visited, stack)
        stack.insert(0, v)

    def topological_sort(self):
        """
        Topological sort of the graph. 
        Uses the recursive function topological_sort_util.
        :return: [list] of nodes (int/char)
        """
        visited = dict.fromkeys(self.graph, False)
        stack = []

        for v in self.graph:
            if not visited[v]:
                self.topological_sort_util(v, visited, stack)
        return stack

    def get(self):
        return self.graph

    def __len__(self):
        """
        Returns the number of nodes in the graph.
        :return: [int] total number of nodes
        """
        return len(self.graph)

    def __str__(self):
        _str = ""
        for v in self.graph:
            _str += str(v) + ' -> '
            for u in self.graph[v]:
                _str += str(u) + ' '
            _str += '\n'
        return _str