# python 3

import unittest
from q2_kth_elem_linkedList_tatjana import *
from random import randint


class TestsKthElement(unittest.TestCase):
    def setUp(self):
        pass

    def test_emptyList(self):
        self.assertEqual(kth_element(None, 0), None)

    def test_example1_sequentialIntegers(self):
        l = List()
        for i in range(1, 11):
            l.append(Node(i))
        for n in range(10):
            kth_node = kth_element(l, n)
            self.assertEqual(kth_node.val, 10-n)

    def test_example2_randomIntegers(self):
        l, l_test = List(), []
        for _ in range(5):
            rand_int = randint(0, 9)
            l.append(Node(rand_int))
            l_test.append(rand_int)
        for n in range(5):
            kth_node = kth_element(l, n)
            self.assertEqual(kth_node.val, l_test[-n-1])


if __name__ == '__main__':
    unittest.main()