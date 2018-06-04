# Python 3
import unittest
from io import StringIO
from unittest.mock import patch
from q1 import print_ancestors, Node


class TestsPrintAncestors(unittest.TestCase):
    def setUp(self):
        pass

    def test1_empty_tree(self):
        with patch('sys.stdout', new=StringIO()) as _output:
            print_ancestors(None, None)
            self.assertEqual(_output.getvalue().strip(), '')

    def test2_example1(self):
        ch11 = Node(2, Node(1), Node(6))
        ch1 = Node(3, ch11, Node(5))
        ch2 = Node(4, right=Node(8))
        root = Node(7, ch1, ch2)
        with patch('sys.stdout', new=StringIO()) as _output:
            print_ancestors(root, 6)
            self.assertEqual(_output.getvalue().strip(), '2 3 7')
        with patch('sys.stdout', new=StringIO()) as _output:
            print_ancestors(root, 8)
            self.assertEqual(_output.getvalue().strip(), '4 7')
        with patch('sys.stdout', new=StringIO()) as _output:
            print_ancestors(root, 5)
            self.assertEqual(_output.getvalue().strip(), '3 7')
        with patch('sys.stdout', new=StringIO()) as _output:
            print_ancestors(root, 7)
            self.assertEqual(_output.getvalue().strip(), '')

    def test3_example2(self):
        ch1 = Node(value=5, left=Node(value=50), right=Node(value=9))
        ch2 = Node(value=15)
        root = Node(value=10, left=ch1, right=ch2)
        with patch('sys.stdout', new=StringIO()) as _output:
            print_ancestors(root, 9)
            self.assertEqual(_output.getvalue().strip(), '5 10')
        with patch('sys.stdout', new=StringIO()) as _output:
            print_ancestors(root, 15)
            self.assertEqual(_output.getvalue().strip(), '10')
        with patch('sys.stdout', new=StringIO()) as _output:
            print_ancestors(root, 10)
            self.assertEqual(_output.getvalue().strip(), '')


if __name__ == '__main__':
    unittest.main()
