#!/usr/bin/python3
import unittest

from code import Parking


class ParkingTest(unittest.TestCase):
    def test_empty_parking(self):
        self.assertListEqual(Parking([], []).get_moves(), [])

    def test_parking_size_1(self):
        self.assertListEqual(Parking([0], [0]).get_moves(), [])

    def test_parking_size_2(self):
        self.assertListEqual(Parking([0, 1], [1, 0]).get_moves(), [(1, 0)])

    def test_parking_equal_start_end_states(self):
        self.assertListEqual(Parking([0, 1, 2, 3], [0, 1, 2, 3]).get_moves(),
                             [])

    def test_parking_basic(self):
        self.assertListEqual(Parking([1, 2, 0, 3], [3, 1, 2, 0]).get_moves(),
                             [(2, 2), (1, 1), (3, 0)])

    def test_incorrect_data_types(self):
        self.assertRaises(TypeError, Parking, {1, 2, 3, 0}, {1, 2, 3, 0})
        self.assertRaises(TypeError, Parking, None, None)

    def test_incorrect_data_values_no_empty_slot(self):
        self.assertRaises(ValueError, Parking, [1, 2, 3, 4], [1, 2, 3, 0])
        self.assertRaises(ValueError, Parking, [1, 2, 3, 0], [1, 2, 3, 4])

    @unittest.skip  # TODO: should we check this?
    def test_incorrect_data_values_two_empty_slots(self):
        self.assertRaises(ValueError, Parking, [1, 2, 0, 0], [0, 0, 1, 2])

    def test_incorrect_data_values_diff_cars_in_start_end(self):
        self.assertRaises(ValueError, Parking, [0, 1, 2, 3], [0, 1, 2, 4])

    def test_incorrect_data_sizes(self):
        self.assertRaises(ValueError, Parking, [1, 2, 0], [1, 2, 3, 0])


if __name__ == "__main__":
    unittest.main()
