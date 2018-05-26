import unittest
from time import time
from task2 import SinglyLinkedList


class TestLinkedList(unittest.TestCase):
    def _test_list(self, a):
        '''
        Create SinglyLinkedList with a as initial list and check all values from kth_to_last function.
        :param a: list with values
        :return:
        '''
        linked_list = SinglyLinkedList(a)
        for i, x in enumerate(a[::-1]):
            self.assertEqual(linked_list.find_kth_to_last(i), x)

    def test_values1(self):
        self._test_list([1, 2, 3, 5, 8, 13, 21])

    def test_values2(self):
        self._test_list(['a', 'b', 'c', 'd'])

    def test_single_value(self):
        self._test_list([0])

    def test_empty(self):
        self._test_list([])

    def test_boundaries(self):
        linked_list = SinglyLinkedList([1, 2, 3])
        self.assertEqual(linked_list.find_kth_to_last(-1), None)
        self.assertEqual(linked_list.find_kth_to_last(3), None)
        self.assertEqual(linked_list.find_kth_to_last(100), None)

if __name__ == '__main__':
    unittest.main()

