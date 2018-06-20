# Python 3
import itertools


def breadth_first_shallowest(ptr):
    """
    Returns a pointer to the breadth first node that has no/single child.
    :param ptr: 
    :return: [Node]
    """
    if ptr is None:
        return None
    if ptr.left is None or ptr.right is None:
        return ptr
    parent_left = breadth_first_shallowest(ptr.left)
    parent_right = breadth_first_shallowest(ptr.right)

    return parent_left if parent_left.depth <= parent_right.depth \
        else parent_right


class Node:
    """
    Implements a binary tree/node data structure.
    Each instance of this class has value (int), two pointers,
    pointer to its parent, and its depth in the tree.
    The root node is at depth 0, his children and 1, and so on.
    """
    def __init__(self, value=None, left=None, right=None, parent=None, depth=0):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.depth = depth

    def __str__(self, level=0):
        _str = "\t"*level + repr(self.value) + '\n'
        if self.left is not None:
            _str += self.left.__str__(level=level+1)
        if self.right is not None:
            _str += self.right.__str__(level=level+1)
        return _str

    def __repr__(self):
        return '<node/tree>'

    def insert(self, value, left=None):
        """
        Creates new Node with the given value, and:
        (1) makes it a left/right child of self, if left is True or False, respectively;
        (2) if left is None, the new node is added s.t. self remains balanced.
        In the former case, if there is an existing child (left/right), it will be overwritten.
        :param value: [int]
        :param left: [bool|None] True/False if the new node shall be left/right child, respectively
        or None if the new node shall be added s.t. the current tree remains balanced
        :return: [Node] pointer to the new node
        """
        if left is None:
            # find the parent of the node to be added
            new_parent = breadth_first_shallowest(self)
            new_node = Node(value=value, left=None, right=None, parent=new_parent,
                            depth=0 if new_parent is None else new_parent.depth + 1)
            if new_parent is not None:
                if new_parent.left is None:
                    new_parent.left = new_node
                else:
                    new_parent.right = new_node
        else:
            new_node = Node(value, parent=self, depth=self.depth+1)
            if left:
                self.left = new_node
            else:
                self.right = new_node
        return new_node


def print_ancestors(tree, key):
    """
    Given a binary tree and a key, it prints the ancestors of the given key,
    starting from the lowest
    Assumption: None is a valid value of Node
    Assumption: The keys are unique
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


def ancestors(tree, key):
    """
    Functionality identical to 'print_ancestors' (see above), whereas here we return a list of nodes,
    rather than printing the ancestors' values
    Assumption: The keys are unique
    :param tree: [Node] binary tree (not necessarily BST)
    :param key: [int] value whose ancestors of the given tree are printed
    :return: [Node|None] list of nodes or None if key not found
    """
    if tree is None:
        return None
    if tree.value == key:
        _ancestors = []
        ptr = tree.parent
        while ptr is not None:
            _ancestors.append(ptr)
            ptr = ptr.parent
        return _ancestors
    return ancestors(tree.left, key) or ancestors(tree.right, key)


def str_values(nodes):
    """
    Given list of objects of Node, it returns string of their keys
    If nodes is None, it returns empty string
    :param nodes: [list(Nodes)] where each object Node has value
    :return: [string]
    """
    if nodes is None:
        return ""
    return " ".join(str(node.value) for node in nodes)


def is_in(tree, key):
    """
    Returns True if tree has node with value key, False otherwise.
    Assumption: None is a valid value of Node
    :param tree: [Node] tree to be searched
    :param key: [int] value to be searched in tree
    :return: [bool] True/False
    """
    if tree is None:
        return False
    if tree.value == key or is_in(tree.left, key) or is_in(tree.right, key):
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
    :return: [int/None] returns the value of the LCA, None if LCA is not found
    """
    if tree is None:  # base case: tree is None
        return None

    if len(keys) != 2:
        raise NotImplementedError

    # special case where key[0] == key[1] and the parent may have only one child (key[0])
    if keys[0] == keys[1] and \
        (tree.left is not None and tree.left.value == keys[0]) or \
            (tree.right is not None and tree.right.value == keys[0]):
        return tree.value

    # base case: we came to a (half)leaf, or one of the keys (thus no ancestor on this branch)
    if tree.value in keys or tree.left is None or tree.right is None:
        return None

    for i in range(len(keys)):  # O(2)
        if keys[i] in [tree.left.value, tree.right.value] and \
                (is_in(tree.left, keys[len(keys)-i-1]) or is_in(tree.right, keys[len(keys)-i-1])):
            return tree.value

    return lowest_common_ancestor(tree.left, keys) or lowest_common_ancestor(tree.right, keys)
