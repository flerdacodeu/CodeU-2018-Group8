#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from question2 import LinkedList, kth_to_last


class TestKthToLast(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        for number in range(10):
            self.linked_list.add(number)

    def test_kth_to_last(self):
        for k in range(10):
            self.assertEqual(kth_to_last(self.linked_list, k), len(self.linked_list) - k - 1)

    def test_negative_k(self):
        self.assertIsNone(kth_to_last(self.linked_list, -1))

    def test_large_k(self):
        self.assertEqual(kth_to_last(self.linked_list, 1e5), self.linked_list.root.value)


if __name__ == '__main__':
    unittest.main()
