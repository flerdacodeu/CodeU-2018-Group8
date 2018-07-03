import unittest
import Task


class TestTask(unittest.TestCase):

    def setUp(self):
        self.grid = [["F", "T", "F", "T"], ["T", "T", "F", "F"], ["F", "F", "T", "F"], ["F", "F", "T", "F"]]
        self.grid1 = [["T", "T"], ["T", "F"], ["F", "T"]]
        self.grid2 = [["T"]]
        self.grid3 = [["T", "T", "T"], ["T", "T", "T"]]
        self.grid4 = [["F"]]
        self.grid5 = [["F", "F", "F"], ["F", "F", "F"]]
        self.grid6 = []
        self.grid7 = [["T",  "T", "F", "F", "F"], ["F",  "T", "F", "F", "T"], ["T",  "F", "F", "T", "T"],
                      ["F",  "F", "F", "F", "F"], ["T",  "F", "T", "F", "T"]]
        self.grid8 = [["T", "F"], ["F", "T"]]
        self.grid9 = [["F", "T"], ["T", "F"]]
        self.grid10 = [["T", "F"], ["T", "F"]]

    def test_count_islands(self):
        self.assertEquals(Task.count_islands(self.grid), 3)
        self.assertEquals(Task.count_islands(self.grid1), 2)
        self.assertEquals(Task.count_islands(self.grid2), 1)
        self.assertEquals(Task.count_islands(self.grid3), 1)
        self.assertEquals(Task.count_islands(self.grid4), 0)
        self.assertEquals(Task.count_islands(self.grid5), 0)
        self.assertEquals(Task.count_islands(self.grid6), 0)
        self.assertEquals(Task.count_islands(self.grid7), 6)
        self.assertEquals(Task.count_islands(self.grid8), 2)
        self.assertEquals(Task.count_islands(self.grid9), 2)
        self.assertEquals(Task.count_islands(self.grid10), 1)
