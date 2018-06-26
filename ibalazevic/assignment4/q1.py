import unittest

def count_islands(nrows, ncols, grid):
    """
    A method that finds all the islands in a 2D grid 
    and counts them up. Each cell in the grid is either 
    land or water. Two cells belong to the same island 
    if they are both land and are adjacent horizontally 
    or vertically.
        - nrows - int, number of grid rows
        - ncols - int, number of grid columns
        - grid - list of lists of booleans, a 2D grid
                 where True indicates land and False
                 water
        Returns: int, number of found islands
    """
    islands = []
    shifts = ((0, 1), (1, 0), (-1, 0), (0, -1))
    visited_positions = set()
    for posx in range(nrows):
        for posy in range(ncols):
            curr_island = []
            pos = (posx, posy)
            _find_islands(nrows, ncols, grid, pos, shifts, 
                  curr_island, islands, visited_positions)
            if curr_island:
                islands.append(curr_island)
    return len(islands)
    


def _find_islands(nrows, ncols, grid, pos, shifts, 
                 curr_island, islands, visited_positions):
    """
    A recursive helper method to finds all the islands in a 
    2D grid.
        - nrows - int, number of grid rows
        - ncols - int, number of grid columns
        - grid - list of lists of booleans, a 2D grid
                 where True indicates land and False
                 water
        - pos - tuple of ints, current position in the grid
        - shifts - list of tuples, the 4 possible moves moves
                   from the current position
        - curr_island - list, a list of positions belonging
                        to the current island
        - islands - list, a list of all the islands found so far
        - visited_positions - set of tuples, keeps track of all
                              the True positions we've visited
    """
    if nrows > pos[0] >= 0 and ncols > pos[1] >= 0:
        if grid[pos[0]][pos[1]] and pos not in visited_positions:
            curr_island.append(pos)
            visited_positions.add(pos)
            for shift in shifts:
                _find_islands(nrows, ncols, grid, (pos[0]+shift[0], 
                              pos[1]+shift[1]), shifts, curr_island, 
                              islands, visited_positions)
 


class CountIslandsTest(unittest.TestCase):
    
    def test_base(self):
        grid = [[False, True, False, True], [True, True, False, False], 
                [False, False, True, False], [False, False, True, False]]
        self.assertEqual(count_islands(4, 4, grid), 3)
  
    def test_empty(self):
        grid = [[]]
        self.assertEqual(count_islands(0, 0, grid), 0)

    def test_all_true(self):
        grid = [[True, True, True, True], [True, True, True, True], 
                [True, True, True, True], [True, True, True, True]]
        self.assertEqual(count_islands(4, 4, grid), 1)

    def test_all_false(self):
        grid = [[False, False, False, False], [False, False, False, False], 
                [False, False, False, False], [False, False, False, False]]
        self.assertEqual(count_islands(4, 4, grid), 0)

    def test_diagonal(self):
        grid = [[True, False, False, False], [False, True, False, False], 
                [False, False, True, False], [False, False, False, True]]
        self.assertEqual(count_islands(4, 4, grid), 4)


if __name__ == '__main__':
    unittest.main()
