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


def print_ancestors(root, key):
    """
    Recursive function to print all ancestors of a Node.
    """

    #Base Case
    if root == None:
        return False

    if root.value == key:
        return True

    if (print_ancestors(root.left, key) or print_ancestors(root.right, key)):
        
        #Prints ancestors when found
        print (root.value)
        return True

    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)

print_ancestors(root, 7)
