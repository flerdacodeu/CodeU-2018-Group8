# Python 3
from utils import neighbors, DisjointSet


class Islands:
    """
    Implements a class of list of disjoint sets whose elements are unique integers,
    as well as methods which identify the number of such sets called islands.
    Two unique integers which identify a position of a 2D grid belong to the same 
    island if they are neighbors (see docstring of the function neighbors in module utils).

    Attributes:
        sets    [list of sets] list sets, where each set contains position identifiers (integers).
        width   [int] width of the grid.
        height  [int] height of the grid.
    """

    def __init__(self, grid):
        """
        Given grid of Boolean values, it creates an instance of Islands which contains a collection 
        of sets, each representing an island (see above def. of an island).
        :param grid: [2D bools] where True denotes land, False water
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            raise ValueError
        lands = []
        self.width, self.height = len(grid), len(grid[0])
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j]:
                    lands.append(i * self.width + j)
        self.sets = DisjointSet(lands)
        edges = []
        for x in lands:
            for y in [x-1, x+1, x-self.width, x+self.width]:
                if neighbors(x, y, self.width, self.height):  # if x == y returns False
                    edges.append((x, y))
        for x, y in edges:
            self.sets.union(x, y)
        self.sets.filter()

    def __str__(self):
        _str = ""
        for _set in self.sets.disjointSets:
            _str += _set.__str__() + '; '
        return _str

    def __len__(self):
        return len(self.sets)

    def get_sets(self):
        return self.sets.get()
