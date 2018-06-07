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


def lowest_common_ancestors(root, node1, node2):
    """
    Function to find lowest common ancestor of two nodes.
    """
