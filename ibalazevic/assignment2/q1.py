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

    def print_ancestors(self, key):
        """
        A method for printing all ancestors of a given key.
            - key - int, the node for which we are printing
                    the ancestors.
            Returns: prints the ancestors. If a key is not
                     present in the tree, prints None.
        """
        ancestors = self.find_ancestors(self.root, key, [])
        if ancestors is not None:
            print ", ".join(map(str, ancestors))
        else:
            print None

    def find_ancestors(self, node, key, ancestors):
        """
        A recursive method for finding all ancestors of a 
        given key.
            - node - Node, the current node.
            - key - int, the node for which we are printing
                    the ancestors.
            - ancestors - list, contains the list of all
                          ancestors of the current node.
            Returns: list, the list of ancestors.
        """
        if not node:
            return
        if node.data == key:
            return ancestors

        ancestors.append(node.data)
        if self.find_ancestors(node.left_child, key, ancestors) or\
           self.find_ancestors(node.right_child, key, ancestors):
           return ancestors
        ancestors.pop()
        return None



class BinaryTreeTest(unittest.TestCase):

    def runTest(self):
        self.test_root()
        self.test_middle()
        self.test_leaf()
        self.test_missing_key()
   

    def test_root(self):
        tree = BinaryTree(7)
        tree.insert_left(tree.root, 3)
        tree.insert_right(tree.root, 4)
        tree.insert_left(tree.root.left_child, 2)
        tree.insert_right(tree.root.left_child, 5)
        tree.insert_right(tree.root.right_child, 8)
        tree.insert_left(tree.root.left_child.left_child, 1)
        tree.insert_right(tree.root.left_child.left_child, 6)
        self.assertEqual(tree.find_ancestors(tree.root, 7, []), [])

    def test_middle(self):
        tree = BinaryTree(7)
        tree.insert_left(tree.root, 3)
        tree.insert_right(tree.root, 4)
        tree.insert_left(tree.root.left_child, 2)
        tree.insert_right(tree.root.left_child, 5)
        tree.insert_right(tree.root.right_child, 8)
        tree.insert_left(tree.root.left_child.left_child, 1)
        tree.insert_right(tree.root.left_child.left_child, 6)
        self.assertEqual(tree.find_ancestors(tree.root, 6, []), [7, 3, 2])

    def test_leaf(self):
        tree = BinaryTree(7)
        tree.insert_left(tree.root, 3)
        tree.insert_right(tree.root, 4)
        tree.insert_left(tree.root.left_child, 2)
        tree.insert_right(tree.root.left_child, 5)
        tree.insert_right(tree.root.right_child, 8)
        tree.insert_left(tree.root.left_child.left_child, 1)
        tree.insert_right(tree.root.left_child.left_child, 6)
        self.assertEqual(tree.find_ancestors(tree.root, 8, []), [7, 4])

    def test_missing_key(self):
        tree = BinaryTree(7)
        tree.insert_left(tree.root, 3)
        tree.insert_right(tree.root, 4)
        tree.insert_left(tree.root.left_child, 2)
        tree.insert_right(tree.root.left_child, 5)
        tree.insert_right(tree.root.right_child, 8)
        tree.insert_left(tree.root.left_child.left_child, 1)
        tree.insert_right(tree.root.left_child.left_child, 6)
        self.assertEqual(tree.find_ancestors(tree.root, 10, []), None)


suite = unittest.TestLoader().loadTestsFromModule(BinaryTreeTest())
unittest.TextTestRunner().run(suite)