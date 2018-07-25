import unittest

from code import Parking


class ParkingTest(unittest.TestCase):
    def test_empty_parking(self):
        self.assertEqual(Parking([], []).get_moves(), [])

    def test_parking_size_1(self):
        self.assertEqual(Parking([0], [0]).get_moves(), [])

    def test_parking_size_2(self):
        self.assertEqual(Parking([0, 1], [1, 0]).get_moves(), [(1, 0)])

    def test_parking_equal_start_end_states(self):
        self.assertEqual(Parking([0, 1, 2, 3], [0, 1, 2, 3]).get_moves(), [])

    def test_parking_basic(self):
        self.assertEqual(Parking([1, 2, 0, 3], [3, 1, 2, 0]).get_moves(), [(2, 2), (1, 1), (3, 0)])

    def test_incorrect_data_types(self):
        self.assertRaises(ValueError, Parking, {1, 2, 3, 0}, {1, 2, 3, 0})

    def test_incorrect_data_values(self):
        self.assertRaises(ValueError, Parking, [1, 2, 3, 4], [1, 2, 3, 0])

    def test_incorrect_data_sizes(self):
        self.assertRaises(ValueError, Parking, [1, 2, 0], [1, 2, 3, 0])


if __name__ == "__main__":
    unittest.main()
