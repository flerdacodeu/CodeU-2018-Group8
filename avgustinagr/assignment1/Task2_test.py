import unittest
from Task2 import*

class test_task2(unittest.TestCase):
    """ Unit tests for task2 """
    def setUp(self):
        self.test_list = SLList()
        for node in range(1,11):
            self.test_list.toFront(node)
    def test_kthtolast(self):
        self.assertEquals(self.test_list.kthtolast(10),10)
        self.assertEquals(self.test_list.kthtolast(1), 1)
        self.assertEquals(self.test_list.kthtolast(0), None)
        self.assertEquals(self.test_list.kthtolast(-23), None)
