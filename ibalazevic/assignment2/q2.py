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
        self.ancestor = self.root.data
        self.found = 0

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

    def lowest_common_ancestor(self, node, key1, key2):
        """
        A method for finding the lowest common ancestor of
        two nodes in a binary tree.
            - node - Node, the root node of the tree.
            - key1 - int, value of first of the nodes.
            - key2 - int, value of second of the nodes.
            Returns: int, value of the lowest common
                     ancestor node.
        """
        if not node:
            return None

        if node.data == key1 or node.data == key2:
            return node.data

        left_subtree = self.lowest_common_ancestor(node.left_child, key1, key2)
        right_subtree = self.lowest_common_ancestor(node.right_child, key1, key2)

        if left_subtree and right_subtree:
            return node.data
        elif left_subtree:
            return left_subtree
        else:
            return right_subtree


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
   

    def test_leaves_left(self):
        self.assertEqual(self.tree.lowest_common_ancestor(self.tree.root, 1, 6), 2)

    def test_leaves_both_sides(self):
        self.assertEqual(self.tree.lowest_common_ancestor(self.tree.root, 1, 8), 7)

    def test_combined_left(self):
        self.assertEqual(self.tree.lowest_common_ancestor(self.tree.root, 1, 5), 3)

    def test_middle_both_sides(self):
        self.assertEqual(self.tree.lowest_common_ancestor(self.tree.root, 2, 4), 7)




if __name__ == "__main__":
    unittest.main()