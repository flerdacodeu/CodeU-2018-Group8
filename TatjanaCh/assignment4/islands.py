# Python 3


def neighbors(x, y, width):
    """
    Checks if x and y are neighbors in a grid of given width.
    Two positions x and y are neighbors if they are adjacent horizontally 
    or vertically, but not diagonally.
    :param x: [int] position identifier
    :param y: [int] position identifier
    :param width: [int] width of the grid
    :return: [bool] True if x and y are neighbours, False otherwise
    """
    if min([x, y, width]) < 0:
        raise ValueError
    if (x % width == y % width and abs(x-y) == width) or \
            (x // width == y // width and abs(x-y) == 1):
        return True
    else:
        return False


class Islands:
    """
    Implements a class of list of disjoint sets whose elements are unique integers,
    as well as methods which identify the number of such sets called islands.
    Two unique integers which identify a position of a 2D grid belong to the same 
    island if they are neighbors (see docstring of the above function neighbors).
    """
    def __init__(self, width, height):
        self.setList = []
        self.width = width
        self.height = height

    def __add__(self, x):
        """
        Adds new element x to the sets that represent islands.
        If the new element is neighbor to multiple existing such sets, 
        the corresponding islands are being merged.
        :param x: [int] new element to be added
        :return: [None]
        """
        x_neighbors = []
        for s, S in enumerate(self.setList):
            if any([neighbors(x, y, self.width) for y in S]):
                x_neighbors.append(s)
        if len(x_neighbors) < 1:
            self.setList.append(set([x]))
        elif len(x_neighbors) == 1:
            self.setList[x_neighbors[0]].add(x)
        else:
            new_set = set([x])
            for neighbor_set in x_neighbors:
                new_set.update(self.setList[neighbor_set])
            self.setList = [s for i, s in enumerate(self.setList) if i not in x_neighbors]
            self.setList.append(new_set)

    def traverse(self, grid):
        """
        Given a 2D grid of bool values, it determines the islands 
        (see above for definition of an island)
        :param grid: [2D bool] where True denotes land, False water
        :return: [list of sets] the islands
        """
        if len(grid) == 0:
            return
        self.__init__(height=len(grid), width=len(grid[0]))
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j]:
                    self.__add__(i*self.width + j)
        return self.setList

    def __str__(self):
        _str = ""
        for _set in self.setList:
            _str += _set.__str__() + '; '
        return _str

    def __len__(self):
        return len(self.setList)
