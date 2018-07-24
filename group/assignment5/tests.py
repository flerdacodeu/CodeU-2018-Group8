import unittest

from code import get_alphabet, get_all_alphabets


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

    def test_alphabet_functions_any_character(self):
        self.assertRegexpMatches(''.join(get_alphabet(["äl", "är", "lä", "🐨"])), r'^äl(?:([🐨r])(?!.*\1)){2}$')


class AllAlphabetsTest(unittest.TestCase):

    def test_get_all_alphabets_empty(self):
        self.assertEqual(get_all_alphabets([]), [[]])

    def test_get_all_alphabets_one_empty_word(self):
        self.assertEqual(get_all_alphabets([""]), [[]])

    def test_get_all_alphabets_all_empty_words(self):
        self.assertEqual(get_all_alphabets(["", "", ""]), [[]])

    def test_get_all_alphabets_some_empty_words(self):
        self.assertEqual(get_all_alphabets(["", "", "A"]), [["A"]])

    def test_get_all_alphabets_one_word(self):
        self.assertCountEqual(get_all_alphabets(["abc"]),
                              [list("abc"), list("acb"), list("bac"),
                               list("bca"), list("cab"), list("cba")])

    def test_get_all_alphabets_simple(self):
        self.assertCountEqual(get_all_alphabets(["art", "rat", "cat", "car"]),
                              [list("tarc"), list("atrc")])

    def test_get_all_alphabets_cycle_raises_value_error(self):
        self.assertRaises(ValueError, get_all_alphabets,
                          ["art", "rat", "cat", "car", "rr", "ra"])

    def test_get_all_alphabets_identical_words(self):
        self.assertCountEqual(get_all_alphabets(["ART", "ART", "ART"]),
                              [list("ART"), list("ATR"), list("RAT"),
                               list("RTA"), list("TAR"), list("TRA")])

    def test_alphabet_functions_complicated(self):
        self.assertTrue(
            get_alphabet(["alp", "art", "arm", "rat", "cat", "car"]),
            get_all_alphabets(["alp", "art", "arm", "rat", "cat", "car"]))

    def test_alphabet_functions_any_character(self):
        self.assertIn(
            get_alphabet(["älp", "ärt", "ärm", "rat", "cat", "car"]),
            get_all_alphabets(["älp", "ärt", "ärm", "rat", "cat", "car"]))


if __name__ == "__main__":
    unittest.main()
