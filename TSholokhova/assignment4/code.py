from queue import Queue as queue
import logging
from copy import deepcopy
logging.basicConfig(filename="code.log", filemode='w', level=logging.DEBUG)

class MapPainter():
    """
    Paint every land component on the map with specified color.
    Number of resulting colors is number of land somponents on the map.
    """
    def __init__(self, rows, cols, map):
        """
        :param rows: number of rows
        :param cols: number of columns
        :param map: 2-dimensional array of booleans, where false means water and true means land
        """
        self.rows = rows
        self.cols = cols
        self.map = map
        self.coloring_map = deepcopy(self.map)
        self.colors = 0
        self.paint_map()

    def paint_map(self):
        """
        Paint every land component with specified color.
        :return: None (self.coloring_map is changed)
        """
        for x in range(self.rows):
            for y in range(self.cols):
                if type(self.coloring_map[x][y]) == bool:
                    if self.coloring_map[x][y]:
                        self.colors += 1
                        self.paint_component(x, y, self.colors)
                        logging.debug(self.coloring_map)
                    else:
                        self.coloring_map[x][y] = 0

    def get_adjusted_tiles(self, x0, y0):
        """
       Return all adjacent tiles.
       :param x0, y0: initial tile.
       :return: adjusted tiles
       """
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            x_new = x0 + dx[i]
            y_new = y0 + dy[i]
            if 0 <= x_new < self.rows and 0 <= y_new < self.cols:
                yield (x_new, y_new)

    def paint_component(self, x0, y0, color):
        """
        Paint the component of the (x0, y0) tile with specified color.
        :param x0, y0: initial tile.
        :param color: specified color.
        :return None (self.coloring_map is changed)
        """
        queue_of_tiles = queue()
        queue_of_tiles.put((x0, y0))
        while not queue_of_tiles.empty():
            x_cur, y_cur = queue_of_tiles.get()
            self.coloring_map[x_cur][y_cur] = color
            for (x, y) in self.get_adjusted_tiles(x_cur, y_cur):
                if type(self.coloring_map[x][y]) == bool and self.coloring_map[x][y]:
                    queue_of_tiles.put((x, y))

    def draw_coloring_map(self):
        """
        Draw resulting map using matplotlib.
        """
        import matplotlib.pyplot as plt
        plt.matshow(self.coloring_map)
        plt.show()

def count_islands(rows, cols, map):
    """
    The function return the number of islands
    :param rows: number of rows
    :param cols: number of columns
    :param map: 2-dimensional array of booleans, where false means water and true means land
    :return: number of islands
    """
    map_painter = MapPainter(rows, cols, map)
    return map_painter.colors
'''
MapPainter(4, 5, [[False, True, False, True, False],
                  [True, True, False, True, False],
                  [False, False, False, True, True],
                  [True, True, False, False, False]]).draw_coloring_map()
MapPainter(3, 3, [[True, True, True], [True, True, False], [True, False, True]]).draw_coloring_map()
MapPainter(3, 3, [[True, False, True], [False, True, False], [True, False, True]]).draw_coloring_map()
'''