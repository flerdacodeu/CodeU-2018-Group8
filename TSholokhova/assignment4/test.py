import unittest
from code import MapPainter, count_islands

class TestCountIsands(unittest.TestCase):

    def get_map1(self):
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

    def get_map2(self):
        map = [[True, True, True],
               [True, True, False],
               [True, False, True]]
        rows, cols = 3, 3
        lands_cnt = 2
        coloring_map = [[1, 1, 1],
                        [1, 1, 0],
                        [1, 0, 2]]
        return (rows, cols, map, lands_cnt, coloring_map)

    def get_map3(self):
        map = [[True, False, True],
               [False, True, False],
               [True, False, True]]
        rows, cols = 3, 3
        lands_cnt = 5
        coloring_map = [[1, 0, 2],
                        [0, 3, 0],
                        [4, 0, 5]]
        return (rows, cols, map, lands_cnt, coloring_map)

    def test_map_painter(self):
        for get_map in [self.get_map1, self.get_map2, self.get_map3]:
            *args, _, coloring_map = get_map()
            self.assertEqual(MapPainter(*args).coloring_map, coloring_map)

    def test_count_islands(self):
        for get_map in [self.get_map1, self.get_map2, self.get_map3]:
            *args, lands_cnt, _ = get_map()
            self.assertEqual(count_islands(*args), lands_cnt)

if __name__ == '__main__':
    unittest.main()