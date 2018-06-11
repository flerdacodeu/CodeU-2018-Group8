class Node:
    """ Class Node: Each object has value and a two pointers - for left and right child. """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    """ Class Tree: Has a root of type Node """
    def __init__(self):
        self.root = None

    def add(self, val):
        """ Adds a node to the tree with the help of _add """
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        """ Adds a node to the tree as it would be added in a BST

        :param val: val on the new node
        :param node: root of the tree
        """
        if val < node.val:
            if node.left:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def _find(self, root, val):
        """ Finds a node in a tree by its value.

        :param root: the root of the tree in which we are searching
        :param val: the value of the node we are searching for
        :return: object of type Node or raises KeyError if not found
        """
        if root.val == val:
            return root

        if root.right:
            try:
                n = self._find(root.right, val)
                if n: return n
            except KeyError:
                pass

        if root.left:
            try:
                n = self._find(root.left, val)
                if n: return n
            except KeyError:
                pass

        raise KeyError("Node does not exist")
       # return None

    def find_path_from_to(self, ancestor, end, path, flag_print):
        """ Finds the path from a node (end) to one of its ancestors (ancestor). Does not count end as a part of
        the path.
        ancestor must be an ancestor of end.
        If flag_print is set to True, it prints the path reversed.


        :param ancestor: object: ancestor of node with value end
        :param end: object: end node
        :param path: a stack in which we store the path (from ancestor to the parent of end)
        :param flag_print: flag, which determines whether we should print the reversed path or not (from the parent of
        end to ancestor)
        :return: True if found, False if not
        """
        path.append(ancestor.val)

        if ancestor.val == end.val:
            path.pop()
            if flag_print:
                print path[::-1]
            return True

        if ancestor.left:
            if self.find_path_from_to(ancestor.left, end, path, flag_print):
                return True
            path.pop()

        if ancestor.right:
            if self.find_path_from_to(ancestor.right, end, path, flag_print):
                return True
            path.pop()

        return False

    def print_path_to_root(self, end):
        """ Prints the path from the give node to the root.

        :param end: value of the node
        :return: None (the function is only meant to print the path if the node exists)
        """
        end_node = self._find(self.root, end)
        if end_node:
            path = []
            self.find_path_from_to(self.root, end_node, path, True)

    def _common_ancestor(self, root, _node1, _node2):
        """ Helper function for get_common_ancestor(). (Implemented idea from the group session)
        Takes additional parameter: root.

        :param root:  the root of the tree in which the function will be looking for _node1 / _node2
        :param _node1: object: one of the nodes
        :param _node2: object: the other node
        :return: the value of the first common ancestor of _node1 and _node2
        (Can also return None in case that one of nodes does not exist in the tree but since the function is meant to
        be used as a helper of get_common_ancestor(), which checks for that before calling it, such a return value is
        unlikely.)
        """
        if _node1.val == root.val or _node2.val == root.val:
            return root.val

        if root.left:
            val1 = self._common_ancestor(root.left, _node1, _node2)
        else:
            val1 = None

        if root.right:
            val2 = self._common_ancestor(root.right, _node1, _node2)
        else:
            val2 = None

        if val1 is not None and val2 is not None:
            return root.val

        if val1 is not None:
            return val1
        return val2

    def get_common_ancestor(self, node1, node2):
        """ Finds the first common ancestor of two nodes.
          (If node1 is the parent of node2, returns node1.
          When node1 == node2 it returns the value of node1/node2)

          :param node1: value of first node (not necessarily first ro be found)
          :param node2: value of second node
          :return: value of the first common ancestor (or raises KeyError if the given values don`t exist in the tree)
          """
        _node1 = self._find(self.root, node1)
        _node2 = self._find(self.root, node2)

        if not _node1 or not _node2:
            return None

        return self._common_ancestor(self.root, _node1, _node2)

