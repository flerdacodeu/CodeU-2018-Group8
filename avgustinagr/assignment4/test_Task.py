import unittest
import Task


class TestTask(unittest.TestCase):

    def test_count_islands_general_case(self):
        self.grid = [[False, True, False, True], [True, True, False, False], [False, False, True, False],
                     [False, False, True, False]]
        self.grid1 = [[True, True], [True, False], [False, True]]
        self.grid2 = [[True, True, False, False, False], [False, True, False, False, True],
                      [True, False, False, True, True],
                      [False, False, False, False, False], [True, False, True, False, True]]
        self.assertEquals(Task.count_islands(self.grid), 3)
        self.assertEquals(Task.count_islands(self.grid1), 2)
        self.assertEquals(Task.count_islands(self.grid2), 6)

    def test_one_T_tile(self):
        self.grid = [[True]]
        self.assertEquals(Task.count_islands(self.grid), 1)

    def test_one_F_tile(self):
        self.grid = [[False]]
        self.assertEquals(Task.count_islands(self.grid), 0)

    def test_all_tiles_T(self):
        self.grid = [[True, True, True], [True, True, True]]
        self.assertEquals(Task.count_islands(self.grid), 1)

    def test_all_tiles_F(self):
        self.grid = [[False, False, False], [False, False, False]]
        self.assertEquals(Task.count_islands(self.grid), 0)

    def test_empty_grid_returns_0(self):
        self.grid = []
        self.assertEquals(Task.count_islands(self.grid), 0)

    def test_four_tiles_2_Ts_diagonally(self):
        self.grid = [[True, False], [False, True]]
        self.grid1 = [[False, True], [True, False]]
        self.assertEquals(Task.count_islands(self.grid), 2)
        self.assertEquals(Task.count_islands(self.grid1), 2)

    def test_four_tiles_2_Ts_vertically(self):
        self.grid = [[True, False], [True, False]]
        self.assertEquals(Task.count_islands(self.grid), 1)
