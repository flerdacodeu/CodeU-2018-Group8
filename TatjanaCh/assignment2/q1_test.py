# Python 3
import unittest
from io import StringIO
from unittest.mock import patch
from q1 import *


class TestsPrintAncestors(unittest.TestCase):

    def test_empty_tree(self):
        with patch('sys.stdout', new=StringIO()) as _output:
            print_ancestors(None, None)
            self.assertEqual(_output.getvalue().strip(), '')

    def test_example(self):
        tree = Node(7)
        child1 = tree.insert(3, left=True)
        child2 = tree.insert(4, left=False)
        for value in [2, 5, 1, 6]:
            child1.insert(value)
        child2.insert(8, left=False)

        with patch('sys.stdout', new=StringIO()) as _output:
            print_ancestors(tree, 6)
            self.assertEqual(_output.getvalue().strip(), '2 3 7')
        with patch('sys.stdout', new=StringIO()) as _output:
            print_ancestors(tree, 8)
            self.assertEqual(_output.getvalue().strip(), '4 7')
        with patch('sys.stdout', new=StringIO()) as _output:
            print_ancestors(tree, 5)
            self.assertEqual(_output.getvalue().strip(), '3 7')
        with patch('sys.stdout', new=StringIO()) as _output:
            print_ancestors(tree, 7)
            self.assertEqual(_output.getvalue().strip(), '')

    def test_nonExistingKey(self):
        tree = Node(value=10)
        values = [10, 5, 15, 50, 9]
        for value in values:
            tree.insert(value=value)
        with patch('sys.stdout', new=StringIO()) as _output:
            self.assertFalse(print_ancestors(tree, 100))
            self.assertEqual(_output.getvalue().strip(), '')

    def test_returnType(self):
        tree = None
        self.assertFalse(print_ancestors(tree, None))

        tree = Node(100)
        tree.insert(50, left=True)
        tree.insert(150, left=False)
        self.assertTrue(print_ancestors(tree, 50))  # child
        self.assertTrue(print_ancestors(tree, 100))  # root
        self.assertFalse(print_ancestors(tree, 200))  # nonExistingKey


class TestsAncestors(unittest.TestCase):

    def test_empty_tree(self):
        self.assertEqual(str_values(ancestors(None, None)), '')

    def test_example(self):
        tree = Node(7)
        child1 = tree.insert(3, left=True)
        child2 = tree.insert(4, left=False)
        for value in [2, 5, 1, 6]:
            child1.insert(value)
        child2.insert(8, left=False)

        self.assertEqual(str_values(ancestors(tree, 6)), '2 3 7')
        self.assertEqual(str_values(ancestors(tree, 8)), '4 7')
        self.assertEqual(str_values(ancestors(tree, 5)), '3 7')
        self.assertEqual(str_values(ancestors(tree, 7)), '')

    def test_nonExistingKey(self):
        tree = Node(value=10)
        values = [10, 5, 15, 50, 9]
        for value in values:
            tree.insert(value=value)
        self.assertEqual(str_values(ancestors(tree, 100)), '')

    def test_returnType(self):
        tree = None
        self.assertIsNone(ancestors(tree, None))

        tree = Node(100)
        tree.insert(50, left=True)
        tree.insert(150, left=False)
        self.assertIsNotNone((ancestors(tree, 50)))  # child
        self.assertIsNotNone(ancestors(tree, 100))  # root
        self.assertIsNone(ancestors(tree, 200))  # nonExistingKey


class TestsLCA(unittest.TestCase):

    def test_empty_tree(self):
        self.assertFalse(lowest_common_ancestor(None, [None, None]))

    def test_examples(self):
        tree = Node(7)
        child1 = tree.insert(3, left=True)
        child2 = tree.insert(4, left=False)
        for value in [2, 5, 1, 6]:
            child1.insert(value)
        child2.insert(8, left=False)

        self.assertEqual(lowest_common_ancestor(tree, [1, 5]), 3)
        self.assertEqual(lowest_common_ancestor(tree, [3, 4]), 7)
        self.assertEqual(lowest_common_ancestor(tree, [3, 5]), 7)

        tree = Node(10)
        tree.insert(5, left=True)
        tree.insert(15, left=False)
        tree.insert(50)
        tree.insert(9)

        self.assertEqual(lowest_common_ancestor(tree, [50, 9]), 5)
        self.assertEqual(lowest_common_ancestor(tree, [5, 15]), 10)
        self.assertEqual(lowest_common_ancestor(tree, [50, 15]), 10)
        self.assertEqual(lowest_common_ancestor(tree, [9, 9]), 5)

    def test_returnParent(self):
        tree = Node(7)
        child1 = tree.insert(3, left=True)
        child2 = tree.insert(4, left=False)
        for value in [2, 5, 1, 6]:
            child1.insert(value)
        child2.insert(8, left=False)

        self.assertEqual(lowest_common_ancestor(tree, [1, 1]), 2)
        self.assertEqual(lowest_common_ancestor(tree, [6, 6]), 2)
        self.assertEqual(lowest_common_ancestor(tree, [8, 8]), 4)

    def test_nonExistingKey(self):
        tree = Node(7)
        child1 = tree.insert(3, left=True)
        child2 = tree.insert(4, left=False)
        for value in [2, 5, 1, 6]:
            child1.insert(value)
        child2.insert(8, left=False)

        self.assertIsNone(lowest_common_ancestor(tree, [9, 9]))
        self.assertIsNone(lowest_common_ancestor(tree, [7, 100]))
        self.assertIsNone(lowest_common_ancestor(tree, [1000, 2]))
        self.assertIsNone(lowest_common_ancestor(tree, [None, None]))

    def test_rootHasNoAncestor(self):
        tree = Node(7)
        child1 = tree.insert(3, left=True)
        child2 = tree.insert(4, left=False)
        for value in [2, 5, 1, 6]:
            child1.insert(value)
        child2.insert(8, left=False)

        self.assertIsNone(lowest_common_ancestor(tree, [7, 7]))
        self.assertIsNone(lowest_common_ancestor(tree, [3, 7]))
        self.assertIsNone(lowest_common_ancestor(tree, [1, 7]))
        self.assertIsNone(lowest_common_ancestor(tree, [None, 7]))
        self.assertIsNone(lowest_common_ancestor(tree, [7, 8]))

if __name__ == '__main__':
    unittest.main()
