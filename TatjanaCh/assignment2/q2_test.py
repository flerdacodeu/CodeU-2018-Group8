# Python 3
import unittest
from io import StringIO
from q2 import lowest_common_ancestor, Node


class TestsPrintAncestors(unittest.TestCase):
    def setUp(self):
        pass

    def test1_empty_tree(self):
        self.assertEqual(lowest_common_ancestor(None, [None, None]), False)

    def test2_example1(self):
        ch11 = Node(2, Node(1), Node(6))
        ch1 = Node(3, ch11, Node(5))
        ch2 = Node(4, right=Node(8))
        root = Node(7, ch1, ch2)
        self.assertEqual(lowest_common_ancestor(root, [1, 5]), 3)
        self.assertEqual(lowest_common_ancestor(root, [3, 4]), 7)
        self.assertEqual(lowest_common_ancestor(root, [3, 5]), 7)

    def test3_example(self):
        ch1 = Node(value=5, left=Node(value=50), right=Node(value=9))
        ch2 = Node(value=15)
        root = Node(value=10, left=ch1, right=ch2)
        self.assertEqual(lowest_common_ancestor(root, [50, 9]), 5)
        self.assertEqual(lowest_common_ancestor(root, [5, 15]), 10)
        self.assertEqual(lowest_common_ancestor(root, [50, 15]), 10)
        self.assertEqual(lowest_common_ancestor(root, [9, 9]), 5)

    def test4_returnParent(self):
        ch11 = Node(2, Node(1), Node(6))
        ch1 = Node(3, ch11, Node(5))
        ch2 = Node(4, right=Node(8))
        root = Node(7, ch1, ch2)
        self.assertEqual(lowest_common_ancestor(root, [1, 1]), 2)
        self.assertEqual(lowest_common_ancestor(root, [6, 6]), 2)
        self.assertEqual(lowest_common_ancestor(root, [8, 8]), 4)

    def test5_KeyNotInTree(self):
        ch11 = Node(2, Node(1), Node(6))
        ch1 = Node(3, ch11, Node(5))
        ch2 = Node(4, right=Node(8))
        root = Node(7, ch1, ch2)
        self.assertEqual(lowest_common_ancestor(root, [9, 9]), False)
        self.assertEqual(lowest_common_ancestor(root, [7, 100]), False)
        self.assertEqual(lowest_common_ancestor(root, [1000, 2]), False)
        self.assertEqual(lowest_common_ancestor(root, [None, None]), False)

    def test6_rootHasNoAncestor(self):
        ch11 = Node(2, Node(1), Node(6))
        ch1 = Node(3, ch11, Node(5))
        ch2 = Node(4, right=Node(8))
        root = Node(7, ch1, ch2)
        self.assertEqual(lowest_common_ancestor(root, [7, 7]), False)
        self.assertEqual(lowest_common_ancestor(root, [3, 7]), False)
        self.assertEqual(lowest_common_ancestor(root, [1, 7]), False)
        self.assertEqual(lowest_common_ancestor(root, [None, 7]), False)
        self.assertEqual(lowest_common_ancestor(root, [7, 8]), False)


if __name__ == '__main__':
    unittest.main()

