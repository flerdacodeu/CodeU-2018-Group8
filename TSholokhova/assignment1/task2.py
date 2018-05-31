class Node():
    '''
    Node of SinglyLinkedList saves self value and link to the next Node
    '''
    def __init__(self, value=None, next=None):
        '''
        :param value: value of Node
        :param next: link to next Node
        '''
        self.value = value
        self.next = next


class SinglyLinkedList():
    '''
    Singly Linked List
    '''
    def __init__(self, a=[]):
        '''
        :param a: list (default [])
            List with initial values which contained in linked list firstly
        '''
        self.first = None
        if not len(a):
            return
        self.first = Node(a[0])
        now = self.first
        for value in a[1:]:
            now.next = Node(value)
            now = now.next

    def find_kth_to_last(self, k=0):
        '''
        Find k-th to last element from linked list.
        :param k: int (default 0)
            If k < 0 or k > linked list length the function return None
        :return:
        Value of k-th to last element or None if k is not correct
        '''
        len = 0
        now = self.first
        while now is not None:
            len += 1
            now = now.next
        if k < 0 or k >= len:
            return None
        now = self.first
        for _ in range(len - k - 1):
            now = now.next
        return now.value