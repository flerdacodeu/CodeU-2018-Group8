# python 3
from collections import defaultdict
import copy


def move_element(element, src_set, dest_set):
    """
    If it is in, removes element from src_set, & adds it to dest_set.
    :param element: [any hashable object] 
    :param src_set: [set]
    :param dest_set: [set]
    :return: [None]
    """
    src_set.discard(element)
    dest_set.add(element)


class Graph:
    """
    Implements Directed Graph.
    The Graph representation used is based on the adjacency list.
    Per each node v, we store a list of nodes u, each indicating directed edge from v to u.
    If there is no edge coming from node v and v is node in the graph, the adjacency list of v is an empty list.
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

    def remove_edge(self, u, v):
        """
        If existing, it removes the edge: u->v.
        Note: it does not remove node v.
        :param u: [int/char] node
        :param v: [int/char] node
        :return: None
        """
        if u in self.graph:
            if v in self.graph[u]:
                self.graph[u].pop(self.graph[u].index(v))

    def in_degree(self):
        """
        Calculates the in-degree of each node.
        :return: [dict] of < node, int> pairs, where the latter is the in-degree of node
        """
        _in_degree = dict.fromkeys(self.graph, 0)
        for u in self.graph:
            for v in self.graph:
                _in_degree[v] += self.graph[u].count(v)
        return _in_degree

    def reverse_edges(self):
        """
        Creates a new Graph, whose nodes are copied from the current graph, whereas its edges are reversed.
        :return: [Graph] the reversed-edge graph of the current one.
        """
        g = Graph()
        for v in self.graph:
            for u in self.graph[v]:
                g.add_edge(u, v)
        return g

    def scc_util(self, v, visited, stack):
        """
        Recursive function. Used by scc().
        :param v: [int/char] current node
        :param visited: [dict] of < node, bool> pairs, where the latter is True if the node has been visited
        :param stack: [list] where nodes are appended after traversing their children
        :return: None
        """
        visited[v] = True
        for u in self.graph[v]:
            if not visited[u]:
                self.scc_util(u, visited, stack)
        stack.append(v)

    def scc(self):
        """
        Finds the strongly connected components (SCC) of the graph.
        Time complexity (V: #nodes, E: #edges): O(3*(V + E)) in total
            O(V + E) for first DFS call;
            O(V + E) for reversing the edges;
            O(V + E) for second DFS call.
        Note: It can be further optimized to O(1*(V+E)), see Tarjan’s Algorithm.
        :return: [list if lists of nodes] the SCCs of the graph
        """
        visited = dict.fromkeys(self.graph, False)
        stack = []

        for v in self.graph:
            if not visited[v]:
                self.scc_util(v, visited, stack)
        reversed_graph = self.reverse_edges()
        visited = dict.fromkeys(self.graph, False)

        sccs = []
        while stack:
            v = stack.pop()
            if not visited[v]:
                queue = []
                reversed_graph.dfs_util(v, visited, queue)
                sccs.append(queue)
        return sccs

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
        :param visited: [dict] of < node, bool> pairs, where the latter is True if the node has been visited
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

    def all_topological_sorts_util(self, visited, stack, res, _in_degree):
        """
        Recursive function. Used by all_topological_sorts().
        :param visited: [dict] of < node, bool> pairs, where the latter is True if the node has been visited
        :param res: [list] where current topological traverse is stored
        :param stack: [list of lists] final result, where each topological traverse is appended when completed
        :param _in_degree: [dict] of pairs < node, in_degree> for each node in the graph
        :return: None
        """

        all_found = False

        for v in self.graph:
            if _in_degree[v] == 0 and not visited[v]:
                # decrease in_degree for the adj.nodes of v
                for u in self.graph[v]:
                    _in_degree[u] -= 1

                res.append(v)
                visited[v] = True
                self.all_topological_sorts_util(visited, stack, res, _in_degree)

                # reset for next traverse
                visited[v] = False
                res.pop(res.index(v))
                for u in self.graph[v]:
                    _in_degree[u] += 1

                all_found = True

        if not all_found:
            stack.append(res.copy())

    def all_topological_sorts(self):
        """
        Topological sort of the graph. 
        Uses the recursive function topological_sort_util.
        :return: [list of lists] of nodes (int/char)
        """
        _in_degree = self.in_degree()
        visited = dict.fromkeys(self.graph, False)
        stack, res = [], []
        self.all_topological_sorts_util(visited, stack, res, _in_degree)
        return stack

    def is_cyclic_util(self, v, visited, nodes_recursion):
        """
        Recursive function. Used by is_cyclic().
        :param v: [int/char] current node
        :param visited: [dict] of < node, bool> pairs, where the latter is True if the node has been visited
        :param nodes_recursion: [dict] whose values are boolean
        :return: None
        """
        visited[v] = True
        nodes_recursion[v] = True

        for u in self.graph[v]:
            if not visited[u] and self.is_cyclic_util(u, visited, nodes_recursion):
                return True
            elif nodes_recursion[u]:
                return True
        nodes_recursion[v] = False
        return False

    def is_cyclic(self):
        """
        Checks if the graph contains at least one cycle.
        :return: [bool] True if a cycle is found, False otherwise
        """
        visited = dict.fromkeys(self.graph, False)
        nodes_recursion = dict.fromkeys(self.graph, False)

        for v in self.graph:
            if not visited[v] and self.is_cyclic_util(v, visited, nodes_recursion):
                return True
        return False

    def sub_graph(self, set_vertices):
        """
        Creates a new graph of a (sub)set of the nodes of this graph, 
        and all the edges between this (sub)set of nodes.
        :param set_vertices: [set] nodes to be retained
        :return: [Graph] new object Graph of this class
        """
        _subgraph = Graph()
        for v in self.graph:
            if v in set_vertices:
                for u in self.graph[v]:
                    if u in set_vertices:
                        _subgraph.add_edge(v, u)
        return _subgraph

    def select_component(self, nodes_ids):
        """
        //this creates graph consisting of strongly connected components only and then returns the
        //least indexed vertex among all the strongly connected component graph.
        //it also ignore one vertex graph since it wont have any cycle.
        :param nodes_ids: [list] list of nodes, where the index of a node is its ID
        :return: 
        """
        sc_components = self.scc()
        min_id, min_node, min_component = len(nodes_ids), None, None
        for i, _scc in enumerate(sc_components):
            if len(_scc) == 0:
                continue
            # pick the component which contains a node with lowest id
            for v in _scc:
                if min_id > nodes_ids.index(v):
                    min_node, min_component = v, i
                    min_id = nodes_ids.index(v)
        return min_node, sc_components[min_component] if min_component is not None else None

    @staticmethod
    def unblock(element, _set, _map):
        """
        Static method, specific for the purpose of all_cycles_util(*) function.
        It removes element from _set, as well as the element(s) indicated by _map[element].
        The latter is done recursively.
        :param element: [any hashable object]
        :param _set: [set]
        :param _map: [set]
        :return: 
        """
        _set.discard(element)
        if element in _map:
            for v in _map[element]:
                Graph.unblock(v, _set, _map)
            del _map[element]

    def all_cycles_util(self, start_node, current_node, blocked_set, blocked_map, stack, result):
        """
        Recursive function, used by all_cycles.
        :param start_node: [any hashable object] starting node
        :param current_node: [any hashable object] currently visiting node
        :param blocked_set: [set] set of blocked nodes (for the purpose of time complexity optimization)
        :param blocked_map: [defaultdict(list)] <node, list> indicating which node unblocks others
        :param stack: [list] stack of nodes visited in the current recursion branch
        :param result: [list of lists] where the encountered cycles (lists of nodes) are appended
        :return: [bool] True if cycle was found, False otherwise (& changes are made in result)
        """
        found_cycle = False
        stack.append(current_node)
        blocked_set.add(current_node)
        for neighbor in self.graph[current_node]:
            if neighbor == start_node:  # found cycle
                stack.append(neighbor)
                result.append(copy.deepcopy(stack))
                stack.pop()
                found_cycle = True
            elif neighbor not in blocked_set:
                found_cycle = self.all_cycles_util(start_node, neighbor, blocked_set, blocked_map, stack, result) \
                              or found_cycle
        # mark nodes as (un)blocked, to optimize the time complexity
        if found_cycle:
            self.unblock(current_node, blocked_set, blocked_map)
        else:
            # map: if ANY of neighbors of current_node gets unblocked, unblock current_node as well
            for neighbor in self.graph[current_node]:
                blocked_map[neighbor].append(current_node)
        stack.pop()
        return found_cycle

    def all_cycles(self):
        """
        Implements the Johnson's algorithm for finding all the cycles in a directed graph.
        Time complexity: O(E+V)*(C+1), where E, V, and C denote the number of edges, 
        number of nodes and number of cycles in the graph, respectively.
        Memory complexity: O(E+V+T), where T is the total length of all the cycles in the graph.
        :return: [list of lists] list of found cycles, where the latter is list of nodes 
        """
        blocked_set = set()
        blocked_map = defaultdict(list)
        stack = []
        _all_cycles = []
        vertices = set(self.graph.keys())
        nodes_ids = list(self.graph.keys())
        while len(vertices) > 0:
            _sub_graph = self.sub_graph(vertices)
            start_node, scc_vertices = _sub_graph.select_component(nodes_ids)
            if start_node is not None and scc_vertices is not None:
                selected_scc_graph = self.sub_graph(scc_vertices)
                blocked_set.clear()
                blocked_map.clear()
                selected_scc_graph.all_cycles_util(start_node, start_node,
                                                   blocked_set, blocked_map,
                                                   stack, _all_cycles)
                vertices.remove(start_node)
            else:
                break
        return _all_cycles

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