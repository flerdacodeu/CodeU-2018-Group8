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
        self.assertRegexpMatches(''.join(get_alphabet(["abc"])), r'^(?:([abc])(?!.*\1)){3}$')

    def test_get_alphabet_simple(self):
        self.assertRegexpMatches(''.join(get_alphabet(["art", "rat", "cat", "car"])), r'^(?:([ta])(?!.*\1)){2}rc$')

    def test_get_alphabet_cycle_raises_value_error(self):
        self.assertRaises(ValueError, get_alphabet,
                          ["art", "rat", "cat", "car", "rr", "ra"])

    def test_get_alphabet_identical_words(self):
        self.assertRegexpMatches(''.join(get_alphabet(['ART', 'ART', 'ART'])), r'^(?:([ART])(?!.*\1)){3}$')


if __name__ == "__main__":
    unittest.main()
