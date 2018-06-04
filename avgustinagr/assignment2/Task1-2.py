class Node:
    """    Class Node: Each object has value and a two pointers - for left and right child.    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    """    Class Tree: Has a root of type Node    """
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.add_node(val, self.root)

    def add_node(self, val, node):
        """ Adds nodes to the tree as they would be added in a BST

        :param val: val on the new node
        :param node: root of the tree
        """
        if val < node.val:
            if node.left:
                self.add_node(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self.add_node(val, node.right)
            else:
                node.right = Node(val)

    def find(self, root, val):
        """  Finds a node in a tree by its value.

        :param root: the root of the tree in which we are searching
        :param val: the value of the node we are searching for
        :return: object of type Node or None if not found
        """
        if root.val == val:
            return root

        if root.right is not None:
            n = self.find(root.right, val)
            if n: return n

        if root.left is not None:
            n = self.find(root.left, val)
            if n: return n
        return None

    def find_path_from_to(self, ancestor, end, path, flag_print):
        """ Finds the path to a node from another one, which is its ancestor.

        :param ancestor: object: ancestor node
        :param end: object: end node
        :param path: a stack in which we store the path
        :param flag_print: flag, which determines whether we should print the reversed path or not
        :return: True if found, False if not
        """
        path.append(ancestor.val)

        if ancestor.val == end.val:
            path.pop()
            if flag_print:
                print path[::-1]
            return True

        if ancestor.left is not None:
            if self.find_path_from_to(ancestor.left, end, path, flag_print):
                return True
            path.pop()

        if ancestor.right is not None:
            if self.find_path_from_to(ancestor.right, end, path, flag_print):
                return True
            path.pop()

        return False

    def print_path_to(self, end):
        """ Prints the path from the give node to the root.

        :param end: value of the node
        """
        end_node = self.find(self.root, end)
        if end_node is None: 
            return None
        
        path = []
        self.find_path_from_to(self.root, end_node, path, True)


    def find_common_ancestor(self, node1, node2):
        """ Finds the first common ancestor of two nodes.
        (If node1 is the parent of node2, returns the value of node1)

        :param node1: object: first node
        :param node2: object: second node
        :return: value of the first common ancestor (or None if the given values don`t exist in the tree)
        """
        path1 = []
        path2 = []
        _node1 = self.find(self.root, node1)
        _node2 = self.find(self.root, node2)

        if _node1 is None or _node2 is None: 
            return None

        self.find_path_from_to(self.root, _node1, path1, False)
        self.find_path_from_to(self.root, _node2, path2, False)
        print "path1 :", path1
        print "path2: ", path2
        
        shorter_path = min(len(path1), len(path2))
        
        for ancestor in range (shorter_path):
            if path1[ancestor] != path2[ancestor]:
                    return path1[ancestor-1]
        
        if shorter_path > 0:
            if path1[shorter_path]:
                return path1[shorter_path]
            if path2[shorter_path]:
                return path2[shorter_path]
        return None

