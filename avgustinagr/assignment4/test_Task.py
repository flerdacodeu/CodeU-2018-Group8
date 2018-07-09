import unittest
import Task


class TestTask(unittest.TestCase):

    def setUp(self):
        self.grid = [[False, True, False, True], [True, True, False, False], [False, False, True, False],
                     [False, False, True, False]]
        self.grid1 = [[True, True], [True, False], [False, True]]
        self.grid2 = [[True]]
        self.grid3 = [[True, True, True], [True, True, True]]
        self.grid4 = [[False]]
        self.grid5 = [[False, False, False], [False, False, False]]
        self.grid6 = []
        self.grid7 = [[True, True, False, False, False], [False, True, False, False, True],
                      [True, False, False, True, True],
                      [False, False, False, False, False], [True, False, True, False, True]]
        self.grid8 = [[True, False], [False, True]]
        self.grid9 = [[False, True], [True, False]]
        self.grid10 = [[True, False], [True, False]]

    def test_count_islands_general_case(self):
        self.assertEquals(Task.count_islands(self.grid), 3)
        self.assertEquals(Task.count_islands(self.grid1), 2)
        self.assertEquals(Task.count_islands(self.grid7), 6)

    def test_one_T_tile(self):
        self.assertEquals(Task.count_islands(self.grid2), 1)

    def test_one_F_tile(self):
        self.assertEquals(Task.count_islands(self.grid4), 0)

    def test_all_tiles_T(self):
        self.assertEquals(Task.count_islands(self.grid3), 1)

    def test_all_tiles_F(self):
        self.assertEquals(Task.count_islands(self.grid5), 0)

    def test_empty_grid_returns_0(self):
        self.assertEquals(Task.count_islands(self.grid6), 0)

    def test_four_tiles_2_Ts_diagonally(self):
        self.assertEquals(Task.count_islands(self.grid8), 2)
        self.assertEquals(Task.count_islands(self.grid9), 2)

    def test_four_tiles_2_Ts_vertically(self):
        self.assertEquals(Task.count_islands(self.grid10), 1)
