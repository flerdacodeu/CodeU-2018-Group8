import unittest
from ancestors import Node, print_ancestors, lowest_common_ancestors

class TestAncestors(unittest.TestCase):

    def setUp(self):
        """
        Setting up tree from assignment example.
        """
        self.root = Node(7)
        self.root.left = Node(3)
        self.root.right = Node(4)
        self.root.left.left = Node(2)
        self.root.left.right = Node(5)
        self.root.left.left.left = Node(1)
        self.root.left.left.right = Node(6)
        self.root.right.right = Node(8)

    def test_print_ancestors(self):
        self.assertEqual(print_ancestors(self.root, 5, []), [3, 7])
        self.assertEqual(print_ancestors(self.root, 7, []), True)
        self.assertEqual(print_ancestors(self.root, 4, []), [7])
        self.assertEqual(print_ancestors(self.root, 8, []), [4, 7])



    def test_lowest_common_ancestors(self):
        self.assertEqual(lowest_common_ancestors(self.root, 1, 5), 3)
        self.assertEqual(lowest_common_ancestors(self.root, 1, 7), 7)
        self.assertEqual(lowest_common_ancestors(self.root, 1, 8), 7)
        self.assertEqual(lowest_common_ancestors(self.root, 2, 5), 3)


if __name__ == "__main__":
    unittest.main()
