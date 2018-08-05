#!/usr/bin/python3
import unittest

from code import ParkingLot, ParkingState


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


class ParkingLotTest(unittest.TestCase):
    def test_empty_parking(self):
        self.assertListEqual(ParkingLot([]).get_moves([]), [])

    def test_parking_size_1(self):
        self.assertListEqual(ParkingLot([0], 0).get_moves([0]), [])

    def test_parking_size_2(self):
        self.assertListEqual(ParkingLot([0, 1]).get_moves([1, 0]), [(1, 0)])

    def test_consistent_states(self):
        state1 = ParkingLot([1, 2, 3], 1)
        state2 = ParkingState([3, 2, 1], 1)
        try:
            state1._validate_two_states(state2)
        except ValueError:
            self.fail("Raised ValueError unexpectedly.")

    def test_inconsistent_states_different_elements(self):
        state1 = ParkingLot([1, 2, 3], 1)
        state2 = ParkingState([1, 2, 5], 1)
        self.assertRaises(ValueError, state1._validate_two_states, state2)

    def test_inconsistent_states_size_mismatch(self):
        state1 = ParkingLot([1, 2], 1)
        state2 = ParkingState([1, 2, 3], 1)
        self.assertRaises(ValueError, state1._validate_two_states, state2)

    def test_inconsistent_states_different_empty_slot_symbol(self):
        state1 = ParkingLot([1, 2, 3], 1)
        state2 = ParkingState([1, 2, 3], 2)
        self.assertRaises(ValueError, state1._validate_two_states, state2)

    def test_compare_identical(self):
        state1 = ParkingLot([1, 2, 3], 1)
        state2 = ParkingState([1, 2, 3], 1)
        self.assertEqual(state1._find_diff(state2), set([]))

    def test_compare_different(self):
        state1 = ParkingLot([1, 2, 3], 1)
        state2 = ParkingState([3, 1, 2], 1)
        self.assertEqual(state1._find_diff(state2), {2, 3})

    def test_next_fewer_move_empty_slot_as_target(self):
        lot1 = ParkingLot([1, 2, 3], 1)
        next_move = lot1.get_moves([1, 3, 2])[0]
        self.assertIn(next_move, [(2, 0), (3, 0)])

    def test_next_fewer_move_correct_car(self):
        lot1 = ParkingLot([1, 2, 3], 1)
        next_move = lot1.get_moves([2, 3, 1])[0]
        self.assertEqual(next_move, (2, 0))

    def test_parking_equal_start_end_states(self):
        cars = [0, 1, 2, 3]
        self.assertListEqual(ParkingLot(cars).get_moves(cars), [])

    def test_parking_basic(self):
        parking_lot = ParkingLot([1, 2, 0, 3])
        self.assertListEqual(parking_lot.get_moves([3, 1, 2, 0]),
                             [(2, 2), (1, 1), (3, 0)])

    def test_parking_state_changed(self):
        parking_lot = ParkingLot([1, 2, 0, 3])
        target_state = [3, 1, 2, 0]
        parking_lot.get_moves(target_state)
        self.assertListEqual(parking_lot.state.cars, target_state)

    def test_parking_state_retained(self):
        cars = [1, 2, 0, 3]
        parking_lot = ParkingLot(cars)
        parking_lot.get_moves([3, 1, 2, 0], retain_state=True)
        self.assertListEqual(parking_lot.state.cars, cars)

    def test_constraint_type_error(self):
        constraints = [1, 2, 3]
        self.assertRaises(TypeError, ParkingLot, [1, 2, 3], 1, constraints)

    def test_validate_feasibility_contradictory(self):
        constraints = {2: {3, 4}}
        parking_lot = ParkingLot([1, 2, 3, 4], 1, constraints)
        self.assertRaises(ValueError, parking_lot.get_moves, [4, 1, 2, 3])

    def test_validate_feasibility_ok(self):
        constraints = {0: {4}, 1: {1, 2, 3}}
        parking_lot = ParkingLot([1, 2, 3, 4], 1, constraints)
        try:
            parking_lot.get_moves([4, 1, 2, 3])
        except ValueError:
            self.fail("Raised ValueError unexpectedly.")

    def test_parking_fewer_moves(self):
        cars = [1, 2, 0, 3]
        parking_lot = ParkingLot(cars)
        final = [2, 3, 0, 1]
        self.assertIn(parking_lot.get_moves(final, retain_state=True),
                      [[(1, 2), (2, 0), (3, 1), (1, 3)],
                       [(2, 2), (3, 1), (1, 3), (2, 0)]])

    def test_parking_active_constraint(self):
        cars = [1, 2, 0, 3]
        parking_lot = ParkingLot(cars, 0)
        final = [2, 3, 0, 1]
        # due to the following constraints, there can be 1 set of moves possible
        constraints = {2: {3}}
        parking_lot.update_constraints(constraints)
        self.assertListEqual(parking_lot.get_moves(final),
                             [(3, 2), (1, 3), (2, 0), (3, 1)])

    def test_parking_move_correctly_positioned_car(self):
        # Edge case: move correctly positioned car, due to constraints
        initial = [1, 2, 0, 3]
        final = [2, 1, 0, 3]
        constraints = {2: {3}}
        parking_lot = ParkingLot(initial, 0, constraints)
        self.assertIn(parking_lot.get_moves(final),
                      [[(3, 2), (1, 3), (2, 0), (1, 1), (3, 3)],
                       [(3, 2), (2, 3), (1, 1), (2, 0), (3, 3)]])

    def test_parking_move_correctly_positioned_car_deeper(self):
        initial = [1, 2, 3, 4, 5, 0]
        final = [2, 1, 4, 5, 3, 0]
        constraints = {0: {1, 2},
                       1: {1, 2, 3},
                       2: {3, 4, 5},
                       3: {3, 4, 5},
                       4: {3, 4, 5},
                       5: {2}}
        parking_lot = ParkingLot(initial, 0, constraints)
        self.assertListEqual(parking_lot.get_moves(final),
                             [(2, 5), (3, 1), (4, 2), (5, 3),
                              (3, 4), (1, 1), (2, 0)])

    def test_parking_constraints_with_no_solution(self):
        # normally this configuration would be backtracked
        initial = [0, 1, 3, 4, 5, 2]
        final = [2, 1, 4, 5, 3, 0]
        constraints = {0: {2},
                       1: {1, 2, 3},
                       2: {3, 4, 5},
                       3: {3, 4, 5},
                       4: {3, 4, 5},
                       5: {2}}
        parking_lot = ParkingLot(initial, 0, constraints)
        self.assertIsNone(parking_lot.get_moves(final))


class ParkingLotAllPathsTest(unittest.TestCase):
    def test_parking_all_paths_simple(self):
        parking_lot = ParkingLot([0, 1, 2])
        self.assertCountEqual(parking_lot.get_all_paths([2, 1, 0]),
                              [[(2, 0)],
                               [(1, 0), (2, 1), (1, 2), (2, 0), (1, 1)]])

    def test_parking_all_paths_simple2(self):
        initial = [1, 2, 0, 3]
        final = [2, 1, 0, 3]
        parking_lot = ParkingLot(initial)
        result = parking_lot.get_all_paths(final)
        self.assertIn([(1, 2), (2, 0), (1, 1)], result)
        self.assertIn([(3, 2), (1, 3), (2, 0), (1, 1), (3, 3)], result)
        # checking uniqueness of paths
        self.assertEquals(len(result), len({tuple(path) for path in result}))

    def test_parking_all_paths_from_example(self):
        parking_lot = ParkingLot([1, 2, 0, 3])
        result = parking_lot.get_all_paths([3, 1, 2, 0])
        self.assertIn([(2, 2), (1, 1), (3, 0)], result)
        self.assertIn([(3, 2), (1, 3), (2, 0), (1, 1), (2, 3), (3, 0), (2, 2)],
                      result)
        self.assertEquals(len(result), len({tuple(path) for path in result}))


if __name__ == "__main__":
    unittest.main()
