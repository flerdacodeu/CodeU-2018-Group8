import unittest
from code import MapPainter, count_islands

class TestCountIsands(unittest.TestCase):
    def _map_1_island(self):
        map = [[True, True, True],
               [True, True, True],
               [True, True, True]]
        rows, cols = 3, 3
        lands_cnt = 1
        coloring_map = [[1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1]]
        return (rows, cols, map, lands_cnt, coloring_map)

    def _map_non_square(self):
        map = [[False, True, False, True, False],
               [True, True, False, True, False],
               [False, False, False, True, True],
               [True, True, False, False, False]]
        rows, cols = 4, 5
        lands_cnt = 3
        coloring_map = [[0, 1, 0, 2, 0],
                        [1, 1, 0, 2, 0],
                        [0, 0, 0, 2, 2],
                        [3, 3, 0, 0, 0]]
        return (rows, cols, map, lands_cnt, coloring_map)

    def _map_2_islands(self):
        map = [[True, True, True],
               [True, True, False],
               [True, False, True]]
        rows, cols = 3, 3
        lands_cnt = 2
        coloring_map = [[1, 1, 1],
                        [1, 1, 0],
                        [1, 0, 2]]
        return (rows, cols, map, lands_cnt, coloring_map)

    def _map_max_islands(self):
        map = [[True, False, True],
               [False, True, False],
               [True, False, True]]
        rows, cols = 3, 3
        lands_cnt = 5
        coloring_map = [[1, 0, 2],
                        [0, 3, 0],
                        [4, 0, 5]]
        return (rows, cols, map, lands_cnt, coloring_map)

    def _map_0_islands(self):
        map = [[False] * 4] * 5
        rows, cols = 5, 4
        lands_cnt = 0
        coloring_map = [[0] * 4] * 5
        return (rows, cols, map, lands_cnt, coloring_map)

    def _map_1_row(self):
        map = [[True, False, True, False, True]]
        rows, cols = 1, 5
        lands_cnt = 3
        coloring_map = [[1, 0, 2, 0, 3]]
        return (rows, cols, map, lands_cnt, coloring_map)


    def _map_1_column(self):
        map = [[True], [False], [True], [False], [True]]
        rows, cols = 5, 1
        lands_cnt = 3
        coloring_map = [[1], [0], [2], [0], [3]]
        return (rows, cols, map, lands_cnt, coloring_map)

    def _map_invalid_data_type(self):
        map = [['a'] * 3] * 6
        rows, cols = 6, 3
        lands_cnt = 0
        coloring_map = [[0] * 3] * 6
        return (rows, cols, map, lands_cnt, coloring_map)

    def _map_invalid_shape(self):
        map = [[False] * 3] * 3
        map[1] = [False] * 4
        rows, cols = 3, 3
        lands_cnt = 0
        coloring_map = [[0] * 3] * 3
        return (rows, cols, map, lands_cnt, coloring_map)

    def test_map_painter_1_island(self):
        rows, cols, map, lands_cnt, coloring_map = self._map_1_island()
        self.assertEqual(MapPainter(rows, cols, map).coloring_map, coloring_map)

    def test_count_islands_1_island(self):
        rows, cols, map, lands_cnt, coloring_map = self._map_1_island()
        self.assertEqual(count_islands(rows, cols, map), lands_cnt)

    def test_map_painter_non_square(self):
        rows, cols, map, lands_cnt, coloring_map = self._map_non_square()
        self.assertEqual(MapPainter(rows, cols, map).coloring_map, coloring_map)

    def test_count_islands_non_square(self):
        rows, cols, map, lands_cnt, coloring_map = self._map_non_square()
        self.assertEqual(count_islands(rows, cols, map), lands_cnt)

    def test_map_painter_2_islands(self):
        rows, cols, map, lands_cnt, coloring_map = self._map_2_islands()
        self.assertEqual(MapPainter(rows, cols, map).coloring_map, coloring_map)

    def test_count_islands_2_islands(self):
        rows, cols, map, lands_cnt, coloring_map = self._map_2_islands()
        self.assertEqual(count_islands(rows, cols, map), lands_cnt)

    def test_map_painter_max_islands(self):
        rows, cols, map, lands_cnt, coloring_map = self._map_max_islands()
        self.assertEqual(MapPainter(rows, cols, map).coloring_map, coloring_map)

    def test_count_islands_max_islands(self):
        rows, cols, map, lands_cnt, coloring_map = self._map_max_islands()
        self.assertEqual(count_islands(rows, cols, map), lands_cnt)

    def test_map_painter_0_islands(self):
        rows, cols, map, lands_cnt, coloring_map = self._map_0_islands()
        self.assertEqual(MapPainter(rows, cols, map).coloring_map, coloring_map)

    def test_count_islands_0_islands(self):
        rows, cols, map, lands_cnt, coloring_map = self._map_0_islands()
        self.assertEqual(count_islands(rows, cols, map), lands_cnt)

    def test_map_painter_1_row(self):
        rows, cols, map, lands_cnt, coloring_map = self._map_1_row()
        self.assertEqual(MapPainter(rows, cols, map).coloring_map, coloring_map)

    def test_count_islands_1_row(self):
        rows, cols, map, lands_cnt, coloring_map = self._map_1_row()
        self.assertEqual(count_islands(rows, cols, map), lands_cnt)

    def test_map_painter_1_column(self):
        rows, cols, map, lands_cnt, coloring_map = self._map_1_column()
        self.assertEqual(MapPainter(rows, cols, map).coloring_map, coloring_map)

    def test_count_islands_1_column(self):
        rows, cols, map, lands_cnt, coloring_map = self._map_1_column()
        self.assertEqual(count_islands(rows, cols, map), lands_cnt)

    def test_count_islands_invalid_data_type(self):
        rows, cols, map, lands_cnt, coloring_map = self._map_invalid_data_type()
        self.assertEqual(count_islands(rows, cols, map), -1)

    def test_count_islands_invalid_shape(self):
        rows, cols, map, lands_cnt, coloring_map = self._map_invalid_shape()
        self.assertEqual(count_islands(rows, cols, map), -1)

if __name__ == '__main__':
    unittest.main()