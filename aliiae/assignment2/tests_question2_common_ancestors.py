#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from questions1_2_ancestors import Node, BinaryTree


class TestAncestorsLCA(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()
        self.tree.root = Node(0)
        self.tree.root.left = Node(1)
        self.tree.root.right = Node(2)
        self.tree.root.left.left = Node(3)
        self.tree.root.left.right = Node(4)
        self.tree.root.right.left = Node(5)
        self.tree.root.right.right = Node(6)

    def test_lca(self):
        self.assertEqual(0, self.tree.lowest_common_ancestor(1, 2))
        self.assertEqual(2, self.tree.lowest_common_ancestor(5, 6))

    def test_lca_root(self):
        self.assertEqual(0, self.tree.lowest_common_ancestor(0, 0))

    def test_lca_identical_keys(self):
        self.assertEqual(1, self.tree.lowest_common_ancestor(1, 1))

    def test_lca_parent_child(self):
        self.assertEqual(1, self.tree.lowest_common_ancestor(1, 4))

    def test_lca_invalid_first_key(self):
        self.assertRaises(KeyError, self.tree.lowest_common_ancestor, 1, 100)

    def test_lca_invalid_second_key(self):
        self.assertRaises(KeyError, self.tree.lowest_common_ancestor, 100, 1)

    def test_lca_invalid_both_keys(self):
        self.assertRaises(KeyError, self.tree.lowest_common_ancestor, 100, 100)


if __name__ == '__main__':
    unittest.main()
