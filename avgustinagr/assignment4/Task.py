def _is_valid_land(x, y, grid):
    """ Checks whether position x, y exists in the grid and whether it is a land tile.

    :param x: integer for the row of the tile
    :param y: integer for the column of the tile
    :param grid: the map of islands and water represented as a list of lists with the visited land marked as False
    :return: True is the tile matches the conditions, False if not
    """
    return (x >= 0) and (x < len(grid)) and (y >= 0) and (y < len(grid[0])) and grid[x][y]


def dfs(grid, i, j):
    """ Implements depth first search for every neighbour (excluding the diagonal neighbours) if they`re land and not
    visited.

    :param grid: the map of islands and water represented as a list of lists with the visited land marked as False
    :param i: integer for the row of the tile
    :param j: integer for the column of the tile
    """
    grid[i][j] = False
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if (abs((x + y) - (i + j)) == 1) and _is_valid_land(x, y, grid):
                dfs(grid, x, y)


def count_islands(old_grid):
    """ Uses dfs() to count the connected components in the grid.

    :param old_grid: the map of islands and water represented as a list of lists
    :return: the number of islands from the grid
    """
    grid = list(old_grid)
    count = 0
    for i in range(0, len(grid)):
        for j in range (0, len(grid[0])):
            if old_grid[i][j] and grid[i][j]:
                    dfs(grid, i, j)
                    count += 1
    return count
