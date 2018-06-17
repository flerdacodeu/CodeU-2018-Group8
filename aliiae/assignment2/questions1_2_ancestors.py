#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Q1 - Print Ancestors
Given a binary tree and a key, write a function that prints all the ancestors
of the key in the given binary tree. The tree is NOT a binary search tree
(where the keys are ordered), but an arbitrary binary tree.

Assumptions:
    1. A node is an ancestor to itself, so the solution will return
    the key among other parent values (e.g., for the root it would be [root]).
    2. In case of duplicate keys, return the leftmost one.
    3. If the key is not present in the tree, return an empty list.

Q2 - Common Ancestor
Design an algorithm and write code to find the lowest common ancestor
of two nodes in a binary tree.
Avoid storing additional nodes in a data structure.

Assumptions:
    1. In case of two invalid keys, raises KeyError.
    2. In case of one invalid key, raises KeyError.
"""


class Node:
    def __init__(self, value):
        """Class for a node in a binary tree, with a value and two children."""
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self):
        """Class to store an arbitrary binary tree having a root."""
        self.root = None

    def print_ancestors(self, key):
        """
        Print values of all the ancestors of the key in the binary tree.

        The key itself is not included in the list.
        If the key has duplicates, return the parents of the leftmost one.
        If key is not found in the tree, return an empty list.
        """
        print(self._get_ancestors(key)[1:])

    def lowest_common_ancestor(self, key1, key2):
        """
        Find the lowest common ancestor of two nodes in a binary tree.

        :param key1: Value of the first node.
        :param key2: Value of the second node.
        :return: The value of the lowest common ancestor of the two nodes.
        :raise KeyError: If one or both of the keys are not found in the tree.
        """
        ancestor = self._get_common_ancestor(self.root, (key1, key2))
        if not ancestor:
            raise KeyError(
                'Keys {} and {} are not found in the tree'.format(key1, key2))
        if ancestor.value == key1 and not self._is_ancestor(ancestor, key2):
            raise KeyError('Key {} is not found in the tree'.format(key2))
        if ancestor.value == key2 and not self._is_ancestor(ancestor, key1):
            raise KeyError('Key {} is not found in the tree'.format(key1))
        return ancestor.value

    def _get_ancestors(self, key):
        """Get a list of parent values in the bottom-up order."""
        ancestors = self._find_ancestors_for_key(key, self.root)
        return ancestors if ancestors else []

    def _find_ancestors_for_key(self, key, root):
        """
        Create a list of ancestors for a given key.

        :param key: Value of a node to search for.
        :param root: Root node of a tree.
        :return: List of ancestors for the key.
        """
        if not root:
            return None
        if root.value == key:
            return [root.value]
        left = self._find_ancestors_for_key(key, root.left)
        if left:  # will handle duplicate keys by going to the left side first
            left.append(root.value)
            return left
        right = self._find_ancestors_for_key(key, root.right)
        if right:
            right.append(root.value)
            return right

    def _get_common_ancestor(self, root, keys):
        """
        Find the lowest common ancestor (LCA) of two nodes recursively, O(n).

        The idea is to search for the keys in left & right subtrees,
        and return the current node if they are found in both of them,
        else return the found LCA from one of the subtrees.
        :param keys: Set of the two keys (values of the nodes) kept in a tuple
        for the sake of brevity (less '==' checks).
        """
        if not root or root.value in keys:
            return root
        left_ancestor = self._get_common_ancestor(root.left, keys)
        right_ancestor = self._get_common_ancestor(root.right, keys)
        if left_ancestor and right_ancestor:
            return root
        return left_ancestor or right_ancestor or None

    def _is_ancestor(self, ancestor, key):
        """
        Check whether the key is found below the ancestor.

        :param ancestor: Starting Node.
        :param key: Value of a node to search for.
        :return: Boolean whether the key is found below the ancestor.
        """
        if not ancestor:
            return False
        if ancestor.value == key:
            return True
        return (self._is_ancestor(ancestor.left, key) or
                self._is_ancestor(ancestor.right, key))
