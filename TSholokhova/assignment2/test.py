import unittest
from time import time
from code import BinaryTree, SparseTable

class TestSparseTable(unittest.TestCase):
    def test_build(self):
        self.assertEqual(SparseTable([1, 2])._st, [[0, 1], [0]])
        self.assertEqual(SparseTable([1, 2, 3, 4, 5])._st, [[0, 1, 2, 3, 4], [0, 1, 2, 3], [0, 1]])
        self.assertEqual(SparseTable([5, 4, 3, 2, 1])._st, [[0, 1, 2, 3, 4], [1, 2, 3, 4], [3, 4]])
        self.assertEqual(SparseTable([3, 1, 2, 2, 3, 1])._st, [[0, 1, 2, 3, 4, 5], [1, 1, 2, 3, 5], [1, 1, 5]])

    def test_rmq(self):
        self.assertEqual(SparseTable([3, 2, 3, 1, 2, 0, 1, 2]).get_min(1, 7), 5)
        self.assertEqual(SparseTable([1, 2, 3, 4, 5]).get_min(2, 4), 2)
        self.assertEqual(SparseTable([1, 2, 3, 4, 5]).get_min(0, 4), 0)
        self.assertEqual(SparseTable([5, 4, 3, 2, 1]).get_min(2, 3), 3)
        self.assertEqual(SparseTable([5, 4, 3, 2, 1]).get_min(0, 4), 4)
        self.assertEqual(SparseTable([100]).get_min(0, 0), 0)



class TestBinaryTree(unittest.TestCase):
    def test_build(self):
        bt = BinaryTree([1, 2, 3, 4, 5, 6, 7, 8])
        T = bt.root
        #root values
        self.assertEqual(T.anc, None)
        self.assertEqual(T.value, 1)
        #values of direct descendants
        self.assertEqual(T.L.value, 2)
        self.assertEqual(T.R.value, 3)
        self.assertEqual(T.R.anc.value, 1)
        # other values
        self.assertEqual(T.L.R.anc.value, 2)
        self.assertEqual(T.L.L.L.value, 8)
        self.assertEqual(T.L.L.R, None)

    def test_find_ancestors(self):
        bt = BinaryTree([7, 3, 4, 2, 5, None, 8, 1, 6])
        T = bt.root
        self.assertEqual(bt._find_ancestors(None), [])
        self.assertEqual(bt._find_ancestors(T), [7])
        self.assertEqual(bt._find_ancestors(T.L.L.R), [6, 2, 3, 7])
        self.assertEqual(bt._find_ancestors(T.L.L.L), [1, 2, 3, 7])
        self.assertEqual(bt._find_ancestors(T.R.R), [8, 4, 7])

    def test_dfs(self):
        bt = BinaryTree([7, 3, 4, 2, 5, None, 8, 1, 6])
        self.assertEqual(bt._heights, [3, 2, 3, 1, 2, 0, 1, 2])
        self.assertEqual(list(map(lambda x: x.value, bt._order)), [1, 2, 6, 3, 5, 7, 4, 8])

    def test_LCA(self):
        bt = BinaryTree([7, 3, 4, 2, 5, None, 8, 1, 6])
        T = bt.root
        self.assertEqual(bt.LCA_value(T.L.R, T.L.L.R), 3)
        self.assertEqual(bt.LCA_value(T.L.L, T.R.R), 7)
        self.assertEqual(bt.LCA_value(T.R.R, T.R), 4)
        self.assertEqual(bt.LCA_value(T.L.L.L, T.L), 3)
        self.assertEqual(bt.LCA_value(T, T), 7)


if __name__ == '__main__':
    unittest.main()