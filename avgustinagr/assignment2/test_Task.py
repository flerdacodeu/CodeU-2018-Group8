import unittest
from Task1 import*


class TestTask(unittest.TestCase):
    """ Unit tests for Task1 """
    def setUp(self):
        self.test_tree = Tree()
        for node in 5, 2, 7, 3, 6, 1, 0:
            self.test_tree.add(node)

    def test_sent_anagrams(self):
        self.assertEqual(self.test_tree.print_path_to(4), None)

    def test_find_common_ancestor(self):
        self.assertEquals(self.test_tree.find_common_ancestor(0, 6), 5)
        self.assertEquals(self.test_tree.find_common_ancestor(5, 5), None)
        self.assertEquals(self.test_tree.find_common_ancestor(0, 1), 1)
        self.assertEquals(self.test_tree.find_common_ancestor(1, 3), 2)

