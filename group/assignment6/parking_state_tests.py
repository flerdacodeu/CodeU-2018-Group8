#!/usr/bin/python3
import unittest
from parking_state import ParkingState


class ParkingStateTest(unittest.TestCase):
    def test_empty_state(self):
        self.assertListEqual(ParkingState([], "").cars, [])

    def test_basic_state(self):
        cars = [1, 2]
        state = ParkingState(cars, 1)
        self.assertListEqual(state.cars, cars)

    def test_invalid_empty_spot_symbol_not_present(self):
        self.assertRaises(ValueError, ParkingState, [1, 2, 3], "a")
        self.assertRaises(ValueError, ParkingState, [1, 2, 3], 4)

    def test_invalid_input_two_empty_slots(self):
        self.assertRaises(ValueError, ParkingState, [1, 2, 0, 0], 0)

    def test_no_swap(self):
        state1 = ParkingState([1, 2, 3], 1)
        state1._swap_cars_and_pos(0, 0)
        self.assertEqual(state1.cars, [1, 2, 3])

    def test_swap(self):
        state1 = ParkingState([1, 2, 3], 1)
        state1._swap_cars_and_pos(1, state1._positions[state1.symbol_empty])
        self.assertEqual(state1.cars, [2, 1, 3])

if __name__ == "__main__":
    unittest.main()
