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

    def testReverseEdges(self):
        ground_truth = {'a': [], 'c': ['a', 'r'], 'r': ['a', 't'], 't': ['a']}
        self.assertDictEqual(self.G.reverse_edges().get(), ground_truth)

    def testDepthFirstSearch(self):
        self.assertEqual(self.G.dfs(), ['a', 'r', 'c', 't'])

    def testTopologicalSort(self):
        self.assertEqual(self.G.topological_sort(), ['a', 't', 'r', 'c'])

    def testAllTopologicalSortsOneResult(self):
        self.assertEqual(self.G.all_topological_sorts(), [['a', 't', 'r', 'c']])

    def testAllTopologicalSortsTwoResults(self):
        self.G.remove_edge('a', 't')
        ground_truth = [['a', 't', 'r', 'c'], ['t', 'a', 'r', 'c']]
        self.assertCountEqual(self.G.all_topological_sorts(), ground_truth)

    def testIsNotCyclic(self):
        self.assertFalse(self.G.is_cyclic())

    def testIsCyclic(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 1)
        self.assertTrue(g.is_cyclic())

    def testSCC_noStronglyConnectedComponents(self):
        self.assertEqual(self.G.scc(), [['a'], ['t'], ['r'], ['c']])

    def testSCC_withStronglyConnectedComponents(self):
        self.G.add_edge('r', 'a')
        self.assertEqual(self.G.scc(), [['a', 'r', 't'], ['c']])
        self.G.remove_edge('r', 'a')

    def testNoCycle(self):
        self.assertEqual(len(Graph().all_cycles()), 0)

    def testOneCycle(self):
        g = Graph()
        g.add_edge('a', 'b')
        g.add_edge('b', 'c')
        g.add_edge('c', 'a')
        self.assertEqual(g.all_cycles(), [['a', 'b', 'c', 'a']])

    def testCycle2Nodes(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 1)
        self.assertEqual(g.all_cycles(), [[1, 2, 1]])

    def testTwoCycles(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 1)
        g.add_edge(3, 4)
        g.add_edge(4, 5)
        g.add_edge(5, 1)
        self.assertEqual(g.all_cycles(), [[1, 2, 3, 1], [1, 2, 3, 4, 5, 1]])

    def testThreeJointCycles(self):
        self.G.add_edge('c', 't')
        self.G.add_edge('r', 'a')
        gt = [['r', 'c', 't', 'r'],
              ['a', 'r', 'a'],
              ['a', 'c', 't', 'r', 'a'],
              ['a', 't', 'r', 'a']]
        self.assertCountEqual(self.G.all_cycles(), gt)

    def testExtendedCycle(self):
        g = Graph()
        g.add_edge('a', 'r')
        g.add_edge('a', 't')
        g.add_edge('t', 'r')
        g.add_edge('r', 'a')
        gt = [['a', 'r', 'a'], ['a', 't', 'r', 'a']]
        self.assertCountEqual(g.all_cycles(), gt)

if __name__ == '__main__':
    unittest.main()
