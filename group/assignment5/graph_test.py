# python 3
import unittest
from graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.G = Graph()
        self.G.add_edge('a', 'r')
        self.G.add_edge('a', 't')
        self.G.add_edge('t', 'r')
        self.G.add_edge('r', 'c')
        self.G.add_edge('a', 'c')

    def testEmptyGraph(self):
        self.assertEqual(len(Graph().get()), 0)

    def testDepthFirstSearch(self):
        self.assertEqual(self.G.dfs(), ['a', 'r', 'c', 't'])

    def testTopologicalSort(self):
        self.assertEqual(self.G.topological_sort(), ['a', 't', 'r', 'c'])

if __name__ == '__main__':
    unittest.main()
