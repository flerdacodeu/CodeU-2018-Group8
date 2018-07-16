import unittest
from code import get_alphabet

class AlphabetTest(unittest.TestCase):

    def test_get_alphabet_empty(self):
        self.assertEqual(get_alphabet([]), [])

    def test_get_alphabet_one_empty_word(self):
        self.assertEqual(get_alphabet(['']), [])

    def test_get_alphabet_all_empty_words(self):
        self.assertEqual(get_alphabet(['', '', '']), [])

    def test_get_alphabet_some_empty_words(self):
        self.assertEqual(get_alphabet(['', '', 'A']), ['A'])

    def test_get_alphabet_one_word(self):
        self.assertTrue(tuple(get_alphabet(["abc"])) in
                        {tuple("abc"), tuple("acb"), tuple("bac"),
                         tuple("bca"), tuple("cab"), tuple("cba")})

    def test_get_alphabet_simple(self):
        self.assertTrue(tuple(get_alphabet(["art", "rat", "cat", "car"])) in
                        {tuple("tarc"), tuple("atrc")})

    def test_get_alphabet_cycle_raises_value_error(self):
        self.assertRaises(ValueError, get_alphabet,
                          ["art", "rat", "cat", "car", "rr", "ra"])

    def test_get_alphabet_identical_words(self):
        self.assertTrue(tuple(get_alphabet(['ART', 'ART', 'ART'])) in
                        {tuple('ART'), tuple('ATR'), tuple('RAT'),
                         tuple('RTA'), tuple('TAR'), tuple('TRA')})

    def test_alphabet_functions_any_character(self):
        self.assertTrue(tuple(get_alphabet(["äl", "är", "lä", "🐨"])) in
                        {tuple("älr🐨"), tuple("äl🐨r")})


if __name__ == "__main__":
    unittest.main()
