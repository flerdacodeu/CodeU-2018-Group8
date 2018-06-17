#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from questions1_2_ancestors import BinaryTree, Node


class TestAncestors(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()
        self.tree.root = Node(0)
        self.tree.root.left = Node(1)
        self.tree.root.right = Node(2)
        self.tree.root.left.left = Node(3)
        self.tree.root.left.right = Node(4)
        self.tree.root.right.left = Node(5)
        self.tree.root.right.right = Node(6)

    def test_binary_tree_get_ancestors(self):
        self.assertEqual([2, 0], self.tree._get_ancestors(2))
        self.assertEqual([6, 2, 0], self.tree._get_ancestors(6))
        self.assertEqual([4, 1, 0], self.tree._get_ancestors(4))

    def test_binary_tree_get_ancestors_root(self):
        self.assertEqual([0], list(self.tree._get_ancestors(0)))

    def test_binary_tree_get_ancestors_invalid_key(self):
        self.assertEqual([], list(self.tree._get_ancestors(100)))

    def test_binary_tree_get_ancestors_duplicate_key(self):
        self.assertEqual([6, 2, 0], self.tree._get_ancestors(6))
        self.tree.root.right.left.left = Node(6)
        self.assertEqual([6, 5, 2, 0], self.tree._get_ancestors(6))


if __name__ == '__main__':
    unittest.main()
