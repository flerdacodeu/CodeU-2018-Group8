# Created on 21.05.18, by Tatjana
# tatjana.chavdarova@{epfl,idiap}.ch
##########################################################################
# For testing each node here has an int, but could be a pointer to a object
# python 3
##########################################################################


gl_int = 0  # added for testing convenience


class Node:
    def __init__(self, n=None, ptr=None):
        global gl_int
        self.val = n if n is not None else gl_int
        if n is None:
            gl_int += 1
        self.ptr = ptr

def print_list(l):
    while l is not None:
        print("%d " % l.val, end='', flush=True)
        l = l.ptr
    print()

def kth_element(l, k):
    assert k >= 0, 'orgering numbers are not negative'
    if l is None:
        return None
    tmp, counter = l, 0
    while tmp is not None:
        counter += 1
        tmp = tmp.ptr
    assert k < counter, 'Error: searching for %d-th element, whereas the list has %d elements' % (k, counter)

    for _ in range(counter-k-1):  # move counter-k-1 times
        l = l.ptr
    return l

##########################################################################
# Test 1:
l = None
for _ in range(10): # create the list backwards
    l = Node(ptr=l)
print('Full list:')
print_list(l)
for n in range(10):
    kth_node = kth_element(l, n)
    print('%d-th node has value %d' % (n, kth_node.val))

##########################################################################
# Test 2
l = None
print_list(l)
node = kth_element(l, 0)
if node is not None:
    print(node.val)
else:
    print('empty list')  # otherwise we would have had AssertionError

##########################################################################
# Test 3
from random import randint
l = None
for _ in range(5):
    l = Node(randint(0, 9), l)
print('Full list:')
print_list(l)
for n in range(5):
    kth_node = kth_element(l, n)
    print('%d-th node has value %d' % (n, kth_node.val))