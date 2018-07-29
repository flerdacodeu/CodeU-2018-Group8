#!/usr/bin/python3
import unittest
from code import ParkingLot, ParkingState


class StateTest(unittest.TestCase):

    def test_empty_state(self):
        self.assertListEqual(ParkingState([], '').get(), [])

    def test_basic_state(self):
        _cars = [1, 2]
        _state = ParkingState(_cars, 1)
        self.assertListEqual(_state.get(), _cars)

    def test_invalid_empty_spot_symbol(self):
        self.assertRaises(ValueError, ParkingState, [1, 2, 3], 'a')
        self.assertRaises(ValueError, ParkingState, [1, 2, 3], 4)

    def test_invalid_input_two_empty_slots(self):
        self.assertRaises(ValueError, ParkingState, [1, 2, 0, 0], 0)

    def test_consistent_states(self):
        _state1 = ParkingState([1, 2, 3], 1)
        _state2 = ParkingState([3, 2, 1], 1)
        try:
            _state1.validate_states(_state2)
        except ValueError:
            self.fail("Raised ValueError unexpectedly.")

    def test_inconsistent_states_different_elements(self):
        _state1 = ParkingState([1, 2, 3], 1)
        _state2 = ParkingState([1, 2, 5], 1)
        self.assertRaises(ValueError, _state1.validate_states, _state2)

    def test_inconsistent_states_size_mismatch(self):
        _state1 = ParkingState([1, 2], 1)
        _state2 = ParkingState([1, 2, 3], 1)
        self.assertRaises(ValueError, _state1.validate_states, _state2)

    def test_inconsistent_states_different_empty_slot_symbol(self):
        _state1 = ParkingState([1, 2, 3], 1)
        _state2 = ParkingState([1, 2, 3], 2)
        self.assertRaises(ValueError, _state1.validate_states, _state2)

    def test_compare_identical(self):
        _state1 = ParkingState([1, 2, 3], 1)
        _state2 = ParkingState([1, 2, 3], 1)
        self.assertEqual(_state1.compare(_state2), set([]))

    def test_compare_different(self):
        _state1 = ParkingState([1, 2, 3], 1)
        _state2 = ParkingState([3, 1, 2], 1)
        self.assertEqual(_state1.compare(_state2), set([2, 3]))

    def test_no_swap(self):
        _state1 = ParkingState([1, 2, 3], 1)
        _state1.swap(0)
        self.assertEqual(_state1.get(), [1, 2, 3])

    def test_swap(self):
        _state1 = ParkingState([1, 2, 3], 1)
        _state1.swap(1)
        self.assertEqual(_state1.get(), [2, 1, 3])

    def test_next_move_empty_slot_as_target(self):
        _state1 = ParkingState([1, 2, 3], 1)
        _state2 = ParkingState([1, 3, 2], 1)
        _g = _state1.get_next_move(_state2)
        self.assertIn(next(_g), [(2, 0), (3, 0)])

    def test_next_move_correct_car(self):
        _state1 = ParkingState([1, 2, 3], 1)
        _state2 = ParkingState([2, 3, 1], 1)
        _g = _state1.get_next_move(_state2)
        self.assertEqual(next(_g), (2, 0))


class ParkingLotTet(unittest.TestCase):

    def test_empty_parking(self):
        self.assertListEqual(ParkingLot([]).get_moves([]), [])

    def test_parking_size_1(self):
        self.assertListEqual(ParkingLot([0], 0).get_moves([0]), [])

    def test_parking_size_2(self):
        self.assertListEqual(ParkingLot([0, 1]).get_moves([1, 0]), [(1, 0)])

    def test_parking_equal_start_end_states(self):
        _cars = [0, 1, 2, 3]
        self.assertListEqual(ParkingLot(_cars).get_moves(_cars), [])

    def test_parking_basic(self):
        _parking_lot = ParkingLot([1, 2, 0, 3])
        self.assertListEqual(_parking_lot.get_moves([3, 1, 2, 0]),
                             [(2, 2), (1, 1), (3, 0)])

    def test_parking_state_changed(self):
        _parking_lot = ParkingLot([1, 2, 0, 3])
        _target_state = [3, 1, 2, 0]
        _parking_lot.get_moves(_target_state)
        self.assertListEqual(_parking_lot.get_state(), _target_state)

    def test_parking_state_retained(self):
        _cars = [1, 2, 0, 3]
        _parking_lot = ParkingLot(_cars)
        _parking_lot.get_moves([3, 1, 2, 0], retain_state=True)
        self.assertListEqual(_parking_lot.get_state(), _cars)

    def test_constraint_type_error(self):
        _constraints = [1, 2, 3]
        self.assertRaises(TypeError, ParkingLot, [1, 2, 3], 1, _constraints)

    def test_validate_feasibility_contradictory(self):
        _constraints = {2: set([3, 4])}
        _parking_lot = ParkingLot([1, 2, 3, 4], 1, _constraints)
        self.assertRaises(ValueError, _parking_lot.get_moves, [4, 1, 2, 3])

    def test_validate_feasibility_ok(self):
        _constraints = {0: set([4]), 1: set([1, 2, 3])}
        _parking_lot = ParkingLot([1, 2, 3, 4], 1, _constraints)
        try:
            _parking_lot.get_moves([4, 1, 2, 3])
        except ValueError:
            self.fail("Raised ValueError unexpectedly.")

    def test_parking_active_constraint(self):
        _cars = [1, 2, 0, 3]
        _parking_lot = ParkingLot(_cars, 0)
        _final = [2, 3, 0, 1]
        self.assertIn(_parking_lot.get_moves(_final, retain_state=True),
                             [[(1, 2), (2, 0), (3, 1), (1, 3)],
                              [(2, 2), (3, 1), (1, 3), (2, 0)]])
        # due to the following constraints, there could be one set of moves possible
        _constraints = {2: set([3])}
        _parking_lot.update_constraints(_constraints)
        self.assertListEqual(_parking_lot.get_moves(_final), [(3, 2), (1, 3), (2, 0), (3, 1)])

    def test_parking_move_correctly_positioned_car(self):
        # Edge case: move correctly positioned car, due to constraints
        _initial = [1, 2, 0, 3]
        _final = [2, 1, 0, 3]
        _constraints = {2: set([3])}
        _parking_lot = ParkingLot(_initial, 0, _constraints)
        self.assertListEqual(_parking_lot.get_moves(_final), [(3, 2), (1, 3), (2, 0), (1, 1), (3, 3)])

if __name__ == "__main__":
    unittest.main()

