##########################################################################
# python 3
##########################################################################


class Node:
    def __init__(self, n, next=None):
        self.val = n
        self.next = next


class List:
    def __init__(self):
        self.start = None
        self.end = None  # for constant time append
        self.len = 0

    def append(self, node):
        """
        Appends a single node.
        :param node: [class Node] node to be appended
        :return: None
        """
        if self.len == 0:
            self.start = node
            self.end = node
        else:
            self.end.next = node
            self.end = node
        self.len += 1

    def __str__(self):
        tmp_ptr = self.start
        _str = ""
        while tmp_ptr is not None:
            _str += "%d " % tmp_ptr.val
            tmp_ptr = tmp_ptr.next
        return _str + '\n'


def kth_element(l, k):
    """
    Returns a reference to the k-th to last element of a singly linked list.
    :param l: [List]
    :param k: [int]
    :return: [node/None]
    """
    if l is None or k >= l.len:
        return None
    tmp = l.start
    for _ in range(l.len - k - 1):
        tmp = tmp.next
    return tmp



