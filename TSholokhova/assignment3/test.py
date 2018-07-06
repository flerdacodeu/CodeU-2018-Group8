import unittest
from time import time
from code import Grid, Dictionary, word_search
class TestGrid(unittest.TestCase):
    def _get_letters_adjacent_cells(self, grid, x0, y0):
        """
        Return sorted letters of adjacent cells.
        :param x0, y0: coordinates of initial cell.
        :return: string.
        """
        letters = ''
        for cell in grid.get_adjacent_cells(x0, y0):
            letters = letters + cell['letter']
        return ''.join(sorted(letters))

    def test_init(self):
        grid = Grid(['AAR',
                     'TCD'])
        self.assertEqual(grid.cols, 3)
        self.assertEqual(grid.rows, 2)
        grid = Grid(['AT',
                     'AC',
                     'RD'])
        self.assertEqual(grid.cols, 2)
        self.assertEqual(grid.rows, 3)

    def test_neighbors(self):
        grid = Grid(['AAR',
                     'TCD'])
        letters = self._get_letters_adjacent_cells(grid, 0, 0)
        self.assertEqual(letters, 'ACT')
        letters = self._get_letters_adjacent_cells(grid, 1, 1)
        self.assertEqual(letters, 'AADRT')


class TestDictionary(unittest.TestCase):
    def test_is_word(self):
        d = Dictionary(['CAR', 'CARD', 'CART', 'CAT'])
        self.assertEqual(d.is_word('CAR'), True)
        self.assertEqual(d.is_word('CART'), True)
        self.assertEqual(d.is_word('ABA'), False)
        self.assertEqual(d.is_word('CA'), False)
        self.assertEqual(d.is_word('CATB'), False)
        self.assertEqual(d.is_word(''), False)

    def test_is_prefix(self):
        d = Dictionary(['CAR', 'CARD', 'CART', 'CAT'])
        self.assertEqual(d.is_prefix('CAR'), True)
        self.assertEqual(d.is_prefix('CART'), True)
        self.assertEqual(d.is_prefix('ABA'), False)
        self.assertEqual(d.is_prefix('CA'), True)
        self.assertEqual(d.is_prefix('CATB'), False)
        self.assertEqual(d.is_prefix('C'), True)
        self.assertEqual(d.is_prefix(''), True)

    def test_is_word_cache(self):
        d = Dictionary(['CAR', 'CARD', 'CART', 'CAT'], use_cache=True)
        d.add_letter_cache('C')
        d.add_letter_cache('A')
        d.add_letter_cache('R')
        self.assertEqual(d.is_word(), True)   # word = CAR
        d.add_letter_cache('A')
        self.assertEqual(d.is_word(), False)  # word = CARA
        d.del_letter_cache()
        d.add_letter_cache('T')
        self.assertEqual(d.is_word(), True)   # word = CART
        d.del_letter_cache()
        d.del_letter_cache()
        self.assertEqual(d.is_word(), False)  # word = CA

    def test_is_prefix_cache(self):
        d = Dictionary(['CAR', 'CARD', 'CART', 'CAT'], use_cache=True)
        self.assertEqual(d.is_prefix(), True)   # prefix = ''
        d.add_letter_cache('C')
        self.assertEqual(d.is_prefix(), True)   # prefix = C
        d.add_letter_cache('B')
        self.assertEqual(d.is_prefix(), False)  # prefix = CB
        d.del_letter_cache()
        d.add_letter_cache('A')
        self.assertEqual(d.is_prefix(), True)   # prefix = CA
        d.add_letter_cache('R')
        self.assertEqual(d.is_prefix(), True)   # prefix = CAR
        d.add_letter_cache('A')
        self.assertEqual(d.is_prefix(), False)  # prefix = CARA
        d.del_letter_cache()
        d.add_letter_cache('T')
        self.assertEqual(d.is_prefix(), True)   # prefix = CART
        d.del_letter_cache()
        d.del_letter_cache()
        self.assertEqual(d.is_prefix(), True)   # prefix = CA


class TestWordSearch(unittest.TestCase):
    def test_example(self):
        d = Dictionary(['CAR', 'CARD', 'CART', 'CAT'], use_cache=True)
        grid = Grid(['AAR', 'TCD'])
        set_all_words = word_search(grid, d)
        self.assertEqual({'CAR', 'CARD', 'CAT'}, set_all_words)

    def test_transpose_example(self):
        d = Dictionary(['CAR', 'CARD', 'CART', 'CAT'], use_cache=True)
        grid = Grid(['AT',
                     'AC',
                     'RD'])
        set_all_words = word_search(grid, d)
        self.assertEqual({'CAR', 'CARD', 'CAT'}, set_all_words)

    def test_same_letters(self):
        d = Dictionary(['A', 'A'*4, 'A'*9, 'A'*10], use_cache=True)
        grid = Grid(['AAA',
                     'AAA',
                     'AAA'])
        set_all_words = word_search(grid, d)
        self.assertEqual({'A', 'A'*4, 'A'*9}, set_all_words)


if __name__ == '__main__':
    unittest.main()