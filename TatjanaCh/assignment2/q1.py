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


def print_ancestors(tree, key):
    """
    Given a binary tree and a key, it prints the ancestors of the given key,
    starting from the lowest
    Assumption: None is a valid value of Node
    :param tree: [Node] binary tree (not necessarily BST)
    :param key: [int] value whose ancestors of the given tree are printed
    :return: [bool] True if key is found, False otherwise
    """
    if tree is None:
        return False
    if tree.value == key:
        return True
    if print_ancestors(tree.left, key) or print_ancestors(tree.right, key):
        print(tree.value, end=' ')
        return True
    return False

