"""Python solution for Assignment 2.

This solution makes the following assumptions:
- The tree is not a binary search tree
- The tree is not balanced
- The tree does not store duplicate values
- There cannot be disconnected trees issues, because the LCA method (lca) takes
  values rather than nodes

"""

from collections import deque


class BinaryTreeNode(object):
  """Node of a binary tree. We store pointers to left and right children and to
  the parent node.

  We choose to store only "value", which serves also as key for a given node, to
  simplify the implementation.

  Attributes:
    value: A value to store in the node, also used as key.
    left: A pointer to Node, left child.
    right: A pointer to Node, right child.
    parent: A pointer to Node, parent.
  """

  def __init__(self, value=None, left=None, right=None, parent=None):
    """Inits BinaryTreeNode with a value, left, right, and parent pointers."""
    self.value = value
    self.left = left
    self.right = right
    self.parent = parent


def insert(root, value):
  """Inserts a new Node with the given value in the tree pointed by root.

  It only inserts the new value if it is not already stored in the tree.
  Although the tree is not balanced, we do a BFS and insert the node in the
  first available position. This helps us to keep the height of the tree
  ~ O(log n), but without guarantees.

  (This method is only used to simplify the tree construction during test
  setUp.)

  Args:
    root: Node, the root of the tree.
    value: A value to be inserted.

  Returns:
    Node, the root node of the tree.
  """
  if not root:
    return BinaryTreeNode(value)
  else:
    try:
      get_node(root, value)
    except KeyError:
      d = deque([root])  # FIFO queue
      while d:
        current_node = d.popleft()
        if not current_node.left:
          current_node.left = BinaryTreeNode(value, parent=current_node)
          return root
        if not current_node.right:
          current_node.right = BinaryTreeNode(value, parent=current_node)
          return root
        d.append(current_node.left)
        d.append(current_node.right)


def get_node(root, value):
  """Returns the node corresponding to value in the tree.

  Args:
    root: Node, the root of the tree
    value: Key to search in the tree.

  Returns:
    The Node that corresponds to the key value.

  Raises:
    KeyError: if value not found.
  """
  if not root:
    raise KeyError('Key {} not found in the tree.'.format(value))
  if root.value == value:
    return root
  try:
    left_result = get_node(root.left, value)
    return left_result
  except KeyError:
    return get_node(root.right, value)


def ancestors(root, value):
  """Returns a list with the ancestors of the node that stores value.

  Args:
    root: Node, the root of the tree.
    value: Key to search in the tree.

  Returns:
    A list of node values, the ancestors of the node that stores value (empty
    if the node has no ancestors, i.e., root node, or the key is not stored in
    the tree).
  """
  try:
    node = get_node(root, value)
  except KeyError:
    return []
  else:
    node_ancestors = []
    while node.parent:
      node_ancestors.append(node.parent.value)
      node = node.parent
    return node_ancestors


def print_ancestors(root, value):
  """Prints the ancestors of the node that stores value in the tree.

  Args:
    root: Node, the root of the tree.
    value: Key to search in the tree.
  """
  print 'Ancestors of {}: {}'.format(
      value, ', '.join(str(i) for i in ancestors(root, value)))


def lca(root, value1, value2):
  """Returns the LCA of the nodes corresponding to value1 and value2.

  (LCA stands for lowest common ancestor.)
  It assumes that no parent pointer is available.

  Args:
    root: Node, the root of the tree.
    value1: Key for the first node.
    value2: Key for the second node.

  Returns:
    The LCA (value).

  Raises:
    KeyError: if at least one of the values is not found in the tree.
  """
  try:
    # Check that both values are in the tree first
    node1 = get_node(root, value1)
    node2 = get_node(root, value2)
  except KeyError:
    raise
  else:
    return _lca(root, node1, node2).value


def _lca(root, node1, node2):
  """Find the LCA of two nodes assuming no parent pointers.

  (LCA stands for lowest common ancestor.)

  This method assumes that both node1 and node2 are connected (i.e., nodes of
  the tree pointed by root)

  Assuming a tree (LT and RT stand for left tree and right tree, respectively,
    and x is the root of the tree):

     x
  LT   RT

  If node1.value or node2.value is x.value, then x is the LCA (one node is
    ancestor of the other).
  If node1.value is in the LT and node2.value is in the RT (or vice versa),
    then x is the LCA.
  If node1.value and node2.value are in the LT, then LCA is in the LT.
  If node1.value and node2.value are in the RT, then LCA is in the RT.

  Args:
    root: Node, the root of the tree.
    node1: Key for the first node.
    node2: Key for the second node.

  Returns:
    The LCA (Node).
  """
  if not root:
    return
  if node1.value == root.value or node2.value == root.value:
    return root
  left = _lca(root.left, node1, node2)
  right = _lca(root.right, node1, node2)
  if left and right:
    return root
  if left:
    return left
  return right
