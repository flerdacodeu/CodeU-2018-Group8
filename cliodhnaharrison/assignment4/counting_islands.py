#Using Python 3
import collections

def count_islands(maps):
    """
    Function to loop over the map to find all islands.

    Arguments:
        maps: The grid map of islands and water.

    Returns:
        num_islands: An int that is the number of islands on the map.
    """
    num_islands = 0

    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col]:
                num_islands += 1
                find_land(maps, row, col)

    return num_islands


def neighbours(maps, row, col):
    """
    Returns the valid neighbours around a cell of position (row, col).

    Arguments:
        maps: The grid map of islands and water.
        row: The row the cell is in, X position in grid.
        col: The column the cell is in, Y position in grid.

    Returns:
        coords: A list of the valid neighbours of the cell.
    """
    coords = []

    row_above = row - 1 >= 0
    row_below = row + 1 < len(maps)
    col_behind = col - 1 >= 0
    col_ahead = col + 1 < len(maps[0])

    if row_above:
        coords.append((row - 1, col))
    if row_below:
        coords.append((row + 1, col))
    if col_behind:
        coords.append((row, col - 1))
    if col_ahead:
        coords.append((row, col + 1))

    return coords



def find_land(maps, row, col):
    """
    Breadth first search function to find all land connected to a cell and mark it as visited by changing True to False in the map.

    Arguments:
        maps: The grid map of islands and water.
        row: The row the cell is in, X position in grid.
        col: The column the cell is in, Y position in grid.
    """
    deck = collections.deque([(row, col)])

    while deck:
        curr_x, curr_y = deck.popleft()

        #Set Land tile in map to Water tile to mark it as visited
        maps[curr_x][curr_y] = False
        for new_x, new_y in neighbours(maps, curr_x, curr_y):
            if maps[new_x][new_y]:
                deck.append((new_x, new_y))
