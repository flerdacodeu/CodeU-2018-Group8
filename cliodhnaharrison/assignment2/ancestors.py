#Using Python 3

class Node:

    def __init__(self, value):
        """
        Node class. Each Node has a value, a left pointer and a right pointer.
        Value, left pointer and right pointer are all initially None.
        """
        self.left = None
        self.right = None
        self.value = value


def print_ancestors(root, key, ancestors=[]):
    """
    Recursive function to print all ancestors of a Node.
    Initially passed a tree, a key of a node and an empty list.
    Assumes nodes are not ancestors of themselves.
    Assumes nodes are in the tree.
    """
    #Base Case
    if root == None:
        return False

    if root.value == key:
        return True

    if (print_ancestors(root.left, key, ancestors) or print_ancestors(root.right, key, ancestors)):
        #Adds ancestors to list when found
        ancestors.append(root.value)
        return ancestors

    return False

def lowest_common_ancestors(root, node1, node2):
    """
    Recursive function to find lowest common ancestor of two nodes.
    Passed a tree and two nodes.
    Assumes nodes are present in the tree.
    """
    if root == None:
        return None
    elif (root.value == node1) or (root.value == node2):
        return root.value

    left_tree = lowest_common_ancestors(root.left, node1, node2)
    right_tree = lowest_common_ancestors(root.right, node1, node2)

    if left_tree and right_tree:
        return root.value
    elif left_tree:
        return left_tree
    else:
        return right_tree
