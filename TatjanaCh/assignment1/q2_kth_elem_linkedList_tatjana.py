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

    def print(self):
        tmp_ptr = self.start
        while tmp_ptr is not None:
            print("%d " % tmp_ptr.val, end='', flush=True)
            tmp_ptr = tmp_ptr.next
        print()


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


##########################################################################
# Test 1:
print('---------------------')
l = List()
for i in range(1, 11):
    l.append(Node(i))
print('Full list:')
l.print()
for n in range(10):
    kth_node = kth_element(l, n)
    print('%d-th node has value %d' % (n, kth_node.val))

##########################################################################
# Test 2
print('---------------------')
l = None
node = kth_element(l, 0)
if node is not None:
    print(node.val)
else:
    print('empty list')

##########################################################################
# Test 3
print('---------------------')
from random import randint
l = List()
for _ in range(5):
    l.append(Node(randint(0, 9)))
print('Full list:')
l.print()
for n in range(5):
    kth_node = kth_element(l, n)
    print('%d-th node has value %d' % (n, kth_node.val))
