class DisjointSet:
    """
    Implements a class DisjointSet, which represents a set of disjoint sets.
    Two sets are disjoint if they have no elements in common.
    It uses dict to speed up finding an element of the subsets.

    Attributes:
        disjointSets         List of the disjoint sets.
        element_set_mapping  Dictionary of <element, index of subset> pairs.
    """

    def __init__(self, elements):
        """
        Initially create separate set for each element.
        The dict 'element_set_mapping' will allow for speeding up find.
        :param elements: [list of int]
        :return: None
        """
        self.disjointSets = []
        self.element_set_mapping = {}
        for ind, e in enumerate(elements):
            self.disjointSets.append(self.make_set(e))
            self.element_set_mapping[e] = ind

    @staticmethod
    def make_set(x):
        """
        Create a new set with x (the representative of the set is x)
        :param x: [int]
        :return: [set]
        """
        return set([x])

    def find(self, e):
        """
        Find the index of the set which contains the element x.
        :param e: [int] the element to be found in any subset
        :return: [int] the index of the set within the attribute disjointSets [list]
        """
        return self.element_set_mapping[e] if e in self.element_set_mapping else None

    def union(self, x, y):
        """
        Merge the set to which x and y belong
        :param x: [int] element
        :param y: [int] element
        :return: None
        """
        x_set = self.find(x)
        y_set = self.find(y)
        if x_set is not None and y_set is not None and x_set != y_set:
            # update element_set_mapping
            for e in self.disjointSets[y_set]:
                self.element_set_mapping[e] = x_set
            # extend x_set
            self.disjointSets[x_set].update(self.disjointSets[y_set])
            # delete y_set
            self.disjointSets[y_set] = None

    def filter(self):
        """
        Remove None elements and update element_set_mapping accordingly.
        :return: None
        """
        decrement, to_del = 0, []
        for i, s in enumerate(self.disjointSets):
            if s is None:
                decrement += 1
                to_del.append(i)
            elif decrement > 0:
                for e in s:
                    self.element_set_mapping[e] -= decrement
        for index in sorted(to_del, reverse=True):
            self.disjointSets.pop(index)

    def __len__(self):
        return sum([1 if s is not None else 0 for s in self.disjointSets])

    def get(self):
        return self.disjointSets


def neighbors(x, y, width, height):
    """
    Checks if x and y are neighbors in a grid of given width.
    Two positions x and y are neighbors if they are adjacent horizontally or 
    vertically, but not diagonally. Assumes given position is not neighbor to itself.
    Returns False if x or y are out of the bounds of the grid.
    :param x: [int] position identifier
    :param y: [int] position identifier
    :param width: [int] width of the grid
    :param height: [int] height of the grid (used for checking the arg values)
    :return: [bool] True iff x and y are neighbours, False otherwise
    """
    if width <= 0 or height <= 0:
        raise ValueError
    if not 0 <= x < width * height or not 0 <= y < width * height:
        return False
    if (x % width == y % width and abs(x - y) == width) or \
            (x // width == y // width and abs(x - y) == 1):
        return True
    else:
        return False
