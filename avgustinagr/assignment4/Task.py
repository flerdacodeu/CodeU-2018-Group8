def is_valid(x, y, grid):
    """ Checks whether position x, y exists in the grid and whether it is a land tile.

    :param x: integer for the row of the tile
    :param y: integer for the column of the tile
    :param grid: the map of islands and water represented as a list of lists
    :return: True is the tile matches the conditions, False if not
    """
    return (x >= 0) and (x < len(grid)) and (y >= 0) and (y < len(grid[0])) and (grid[x][y] == "T")


def dfs(grid, i, j, visited):
    """ Implements depth first search for every neighbour (excluding the diagonal neighbours) if they`re land and not
    visited.

    :param grid: the map of islands and water represented as a list of lists
    :param i: integer for the row of the tile
    :param j: integer for the column of the tile
    :param visited: a list of lists containing only True or False values. True if the tile has been visited, False if not
    """
    visited[i][j] = True
    if is_valid(i-1, j, grid) and not visited[i-1][j]:
        dfs(grid, i-1, j, visited)
    if is_valid(i+1, j, grid) and not visited[i+1][j]:
        dfs(grid, i+1, j, visited)
    if is_valid(i, j-1, grid) and not visited[i][j-1]:
        dfs(grid, i, j-1, visited)
    if is_valid(i, j+1, grid) and not visited[i][j+1]:
        dfs(grid, i, j+1, visited)


def count_islands(grid):
    """ Uses dfs() to count the connected components in the grid.

    :param grid: the map of islands and water represented as a list of lists
    :return: the number of islands from the grid
    """
    visited = []
    for i in range (0, len(grid)):
        visited.append([0]*len(grid[0]))
    count = 0
    for i in range (0, len(grid)):
        for j in range (0, len(grid[0])):
            if grid[i][j] == "T" and not visited[i][j]:
                    dfs(grid, i, j, visited)
                    count += 1
    return count
