class Node:
    """ Class Node: every object has a value and a pointer to the next object """
    def __init__(self, val):
        self.val = val
        self.next = None

class SLList:
    """ Singly Linked List class: has a front, which is supposed to be a Node object and a size"""
    def __init__(self):
        self.front = None
        self.size = 0

    def toFront(self, val):
        """ Adds new nodes to the beginning on the linked list. """
        toAdd = Node(val)
        if self.front is not None:
            toAdd.next=self.front
        self.front=toAdd
        self.size += 1

    def kthtolast(self, k):
        """ Finds the kth to the last element of the linked list.

        Assumption 1: We start counting from 1
        Assumption 2: Counting of elements begins from the end of the list despite the fact that the list may have
        been populated with toFront().

        :param k: the number of elements we count from the last
        :return: the value of the kth to the last element
        """

        if k <= 0 or k > self.size:
            return None

        node = self.front
        num = self.size - k
        while num > 0 and node.next is not None:
            node = node.next
            num -= 1
        return node.val
