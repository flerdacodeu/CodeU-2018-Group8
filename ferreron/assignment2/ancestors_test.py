"""Tests for ancestors module."""

import unittest
import ancestors


class AncestorsTest(unittest.TestCase):

  def setUp(self):
    self.t = ancestors.BinaryTreeNode(0)
    # This generates the following BinaryTree:
    #            0
    #     1      .      2
    #  3  .  4       5  .  6
    # 7.8   9.
    for i in range(1, 10):
      ancestors.insert(self.t, i)

  def test_ancestors(self):
    # root node has no ancestors
    self.assertEqual(ancestors.ancestors(self.t, 0), [])
    # non-existing node has no ancestors
    self.assertEqual(ancestors.ancestors(self.t, 15), [])
    # we find all the ancestors for a given value
    self.assertItemsEqual(ancestors.ancestors(self.t, 1), [0])
    self.assertItemsEqual(ancestors.ancestors(self.t, 4), [1, 0])
    self.assertItemsEqual(ancestors.ancestors(self.t, 6), [2, 0])
    self.assertItemsEqual(ancestors.ancestors(self.t, 8), [3, 1, 0])

  def test_lca(self):
    # same node
    self.assertEqual(ancestors.lca_values(self.t, 3, 3), 3)
    # non-existing node
    with self.assertRaises(KeyError):
      ancestors.lca_values(self.t, 7, 10)
    # we find the LCA for two given values
    self.assertEqual(ancestors.lca_values(self.t, 0, 1), 0)
    self.assertEqual(ancestors.lca_values(self.t, 2, 6), 2)
    self.assertEqual(ancestors.lca_values(self.t, 9, 5), 0)
    self.assertEqual(ancestors.lca_values(self.t, 7, 8), 3)

if __name__ == '__main__':
  unittest.main()
