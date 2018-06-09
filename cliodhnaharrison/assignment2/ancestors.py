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
    """
    #Base Case
    if root == None:
        return False

    if root.value == key:
        return True

    if (print_ancestors(root.left, key, ancestors) or print_ancestors(root.right, key, ancestors)):
        #Prints ancestors when found
        ancestors.append(root.value)
        return ancestors

    return False

def lowest_common_ancestors(self, node1, node2):
    """
    Function to find lowest common ancestor of two nodes.
    """
    return None




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)

print (print_ancestors(root, 7))
