import unittest

class Node:
    """
    A class for a node of a binary tree.
        - data - int, the content of a node.
        - left_child - Node, pointer to the left child 
                       of a current node.
        - right_child - Node, pointer to the right child 
                        of a current node.
    """
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class BinaryTree:
    """
    A class representing a binary tree.
        - root_data - int, content of the tree root.
    """
    def __init__(self, root_data):
        self.root = Node(root_data)

    def insert_left(self, node, data):
        """
        A method for inserting a left child of a node.
            - node - Node, the current node.
            - data - int, the data to insert to the left.
        """
        node.left_child = Node(data)

    def insert_right(self, node, data):
        """
        A method for inserting a right child of a node.
            - node - Node, the current node.
            - data - int, the data to insert to the right.
        """
        node.right_child = Node(data)


    def print_ancestors(self, node, key):
        """
        A method for printing all ancestors of a given key.
            - node - Node, the root node of the tree.
            - key - int, the node for which we are printing
                    the ancestors.
            Returns: prints the ancestors. If a key is not
                     present in the tree, returns True,
                     False otherwise.
        """
        if not node:
            return False
        if node.data == key:
            return True

        if self.print_ancestors(node.left_child, key) or\
           self.print_ancestors(node.right_child, key):
           print node.data
           return True
        return False


class BinaryTreeTest(unittest.TestCase):

    def setUp(self):
        self.tree = BinaryTree(7)
        self.tree.insert_left(self.tree.root, 3)
        self.tree.insert_right(self.tree.root, 4)
        self.tree.insert_left(self.tree.root.left_child, 2)
        self.tree.insert_right(self.tree.root.left_child, 5)
        self.tree.insert_right(self.tree.root.right_child, 8)
        self.tree.insert_left(self.tree.root.left_child.left_child, 1)
        self.tree.insert_right(self.tree.root.left_child.left_child, 6)
   

    def test_root(self):
        self.assertEqual(self.tree.print_ancestors(self.tree.root, 7), True)

    def test_middle(self):
        self.assertEqual(self.tree.print_ancestors(self.tree.root, 6), True)

    def test_leaf(self):
        self.assertEqual(self.tree.print_ancestors(self.tree.root, 8), True)

    def test_missing_key(self):
        self.assertEqual(self.tree.print_ancestors(self.tree.root, 10), False)



if __name__ == "__main__":
    unittest.main()