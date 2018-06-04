# Python 3


class Node:
    """
    Implements a binary tree/node data structure.
    Each instance of this class has value (int) and two pointers.
    """
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self, level=0):
        _str = "\t"*level + repr(self.value) + '\n'
        if self.left is not None:
            _str += self.left.__str__(level=level+1)
        if self.right is not None:
            _str += self.right.__str__(level=level+1)
        return _str

    def __repr__(self):
        return '<node/tree>'


def isIn(tree, key):
    """
    Returns True if tree has node with value key, False otherwise.
    Assumption: None is a valid value of Node
    :param tree: [Node] tree to be searched
    :param key: [int] value to be searched in tree
    :return: [bool] True/False
    """
    if tree is None:
        return False
    if tree.value == key or isIn(tree.left, key) or isIn(tree.right, key):
        return True
    return False


def lowest_common_ancestor(tree, keys):
    """
    Given a binary tree and a key, it prints the lowest common ancestor (LCA) of the two given keys
    If they keys[0]&keys[1] do not have a common ancestor (e.g. one is root and ancestor of the other) returns False
    Assumption: None is a valid value of Node
    Assumption: key[0] == key[1] is valid input, returns its parent
    Assumption: keys have unique values
    Key Idea: node n is LCA iff n.left.value in [key1, key2] or n.right.value in [key1, key2]
    :param tree: [Node] binary tree (not necessarily BST)
    :param keys: [int, int] values whose common ancestor we are looking for
    :return: [bool] True if key is found, False otherwise
    """
    if tree is None:  # base case: tree is None
        return False

    if len(keys) != 2:
        raise NotImplementedError

    # special case where key[0] == key[1] and the parent may have only one child (key[0])
    if keys[0] == keys[1] and \
        (tree.left is not None and tree.left.value == keys[0]) or \
            (tree.right is not None and tree.right.value == keys[0]):
        return tree.value

    # base case: we came to a (half)leaf, or one of the keys (thus no ancestor on this branch)
    if tree.value in keys or tree.left is None or tree.right is None:
        return False

    for i in range(len(keys)):  # O(2)
        if keys[i] in [tree.left.value, tree.right.value] and \
                (isIn(tree.left, keys[len(keys)-i-1]) or isIn(tree.right, keys[len(keys)-i-1])):
            return tree.value

    return lowest_common_ancestor(tree.left, keys) or lowest_common_ancestor(tree.right, keys)
