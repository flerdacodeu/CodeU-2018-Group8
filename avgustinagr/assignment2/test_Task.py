import unittest
from Task1 import*


class TestTask(unittest.TestCase):
    """Unit tests for Task1"""
    def setUp(self):
        self.test_tree = Tree()
        for node in 5, 2, 7, 3, 6, 1, 0:
            self.test_tree.add(node)
            """ Creates:
                        5
                    2      7
                  1   3  6
                0            
            """

    def test_print_path_to_root(self):
        self.assertRaises(KeyError, self.test_tree.print_path_to_root, 4)

    def test_get_common_ancestor(self):
        self.assertEquals(self.test_tree.get_common_ancestor(1, 7), 5)
        self.assertEquals(self.test_tree.get_common_ancestor(1, 3), 2)
        self.assertEquals(self.test_tree.get_common_ancestor(2, 2), 2)
        self.assertEquals(self.test_tree.get_common_ancestor(0, 1), 1)
        self.assertEquals(self.test_tree.get_common_ancestor(0, 6), 5)
        self.assertEquals(self.test_tree.get_common_ancestor(5, 5), 5)
        self.assertRaises(KeyError, self.test_tree.get_common_ancestor, 4, 0)
