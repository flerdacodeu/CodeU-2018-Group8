import unittest

class Node:
    """
    A class representing a node of a linked list.
        - data - the content of each node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A class representing a linked list.
    """

    def __init__(self):
        self.head = None

    def append(self, data):
        """
        A method for appending elements to the
        linked list.
            - data - the content of the node to append.
            Returns: None.
        """
        if not self.head:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(data)

    def get_length(self):
        """
        A method to return the length of the linked list.
            Returns: int, linked list length.
        """
        if not self.head:
            return 0
        else:
            length = 1
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
                length += 1
            return length


    def find_kth_to_last(self, k):
        """
        A method for finding kth to last element of
        a linked list.
            - k - int, the content of which node in
                  a list to return.
            Returns: the contents of the kth to last
                     node.
        """
        p1 = self.head
        p2 = self.head
        i = 0
        if k < 0 or self.get_length() <= k or not self.head:
            return None
        while(p1):
            p1 = p1.next
            if i > k:
                p2 = p2.next
            i += 1
        return p2.data

class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.l = LinkedList()
        self.l.append(2)
        self.l.append(3)
        self.l.append(8)
        self.l.append(10)
        self.l.append(1)

    def test_3rd_to_last(self):        
        self.assertEqual(self.l.find_kth_to_last(3), 3)

    def test_last(self):
        self.assertEqual(self.l.find_kth_to_last(0), 1)

    def test_first(self):
        l = LinkedList()
        self.assertEqual(self.l.find_kth_to_last(4), 2)

    def test_empty(self):
        l = LinkedList()
        self.assertEqual(l.find_kth_to_last(2), None)

    def test_negative_k(self):
        self.assertEqual(self.l.find_kth_to_last(-2), None)

    def test_k_equal_list_length(self):
        self.assertEqual(self.l.find_kth_to_last(5), None)

if __name__ == "__main__":
    unittest.main()
