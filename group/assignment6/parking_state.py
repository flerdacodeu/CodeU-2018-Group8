# -*- coding: utf-8 -*-
"""Defines data structures to represent: 
    - a state of a parking lot (ParkingState);
    - a car; as well as 
    - a sequence of moves (List[_MoveType]).
"""

from typing import List, Set, Dict, Hashable, NamedTuple, Generator, Tuple

CarType = Hashable
MoveType = NamedTuple("MoveType", [("car", "CarType"), ("to", int)])


class ParkingState:
    """Implements a wrapper of a list representing the state of a parking lot.

    Attributes:
        cars: The state list of length N, its indices are the N parking slots,
        and its elements are the N-1 cars and the empty slot.
        symbol_empty: A symbol representing the empty slot, any CarType object.
    """

    def __init__(self, input_list: List[CarType], empty_slot: CarType = 0):
        self._validate_state(input_list, empty_slot)
        self.cars = input_list
        self.symbol_empty = empty_slot
        self._positions = {car: index for index, car in enumerate(self.cars)}

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, idx):
        return self.cars[idx]

    @staticmethod
    def _validate_state(state: List[CarType], symbol_empty: CarType):
        """Validates if technical and parking state properties hold for input.

        This includes:
            1) input must be list;
            2) input contains no duplicates;
            3) given the empty slot representation, the input list contains
            exactly one empty slot.

        Args:
            state: List of cars, where car is a CarType object.
            symbol_empty: Symbol of the empty slot.

        Raises:
            TypeError: Property 1 violated.
            ValueError: Property 2 or 3 violated.
        """
        if not isinstance(state, list):
            raise TypeError(f"Unsupported operand type: {type(state)}. "
                            f"Expected list.")

        if len(state) > 0 and state.count(symbol_empty) != 1:
            raise ValueError("Invalid input, expected one empty slot.")

        if len(state) != len(set(state)):
            raise ValueError("Invalid input: duplicate element(s) found.")

    def generate_all_paths(self, current_moves: List[MoveType],
                           target_state: "ParkingState",
                           displaced_cars: Set[CarType], seen_states,
                           constraints: Dict[int, Set[CarType]]) \
            -> Generator[List[MoveType], None, None]:
        """Finds all paths leading from the current state to the target state.

        It does not have a single sequence that has the same parking lot
        configuration (positions of cars in the parking lot) more than once,
        however, different paths can share the same state.

        It uses a heuristic to start traversing feasible cars for the empty slot
        with the target one. That is, it starts with a greedy algorithm and
        backs off to all possible cars in case of constraints that prevent from
        moving any displaced car into the empty place), see more in the
        `_update_displaced_cars` method.

        Args:
            current_moves: A list of moves currently being done.
            target_state: The target arrangement of the cars.
            displaced_cars: A set of cars that are not in their right positions.
            seen_states: A set of states that have already been visited in the
            current path.
            constraints: A map of constraints telling which cars (values)
            can be moved to which slots (keys).

        Yields:
            List of car moves (car, target_position).
        """
        if not displaced_cars:
            yield current_moves.copy()
            return

        state = tuple(self.cars)
        if state in seen_states:
            return
        seen_states.add(state)

        empty_position = self._positions[self.symbol_empty]
        feasible_cars = self._rearrange_feasible_cars(constraints,
                                                      empty_position,
                                                      target_state)
        for next_car in feasible_cars:
            if current_moves and current_moves[-1].car == next_car:
                continue  # a heuristic to not return straight back
            car_moved_to_target, car_was_in_target \
                = self._update_displaced_cars(displaced_cars, empty_position,
                                              next_car, target_state)
            move = self._swap_cars_and_pos(self._positions[next_car],
                                           empty_position)
            current_moves.append(move)
            empty_position = self._positions[self.symbol_empty]
            next_moves = self.generate_all_paths(current_moves, target_state,
                                                 displaced_cars, seen_states,
                                                 constraints)
            yield from next_moves
            self._restore_state(car_moved_to_target,
                                car_was_in_target,
                                current_moves,
                                displaced_cars,
                                empty_position,
                                next_car)
            empty_position = self._positions[self.symbol_empty]
        seen_states.remove(state)

    def _get_feasible_cars(self, constraints: Dict[int, Set[CarType]],
                           position_empty: int) -> Set[CarType]:
        """Returns the set of cars that can be moved to position_empty.

        Args:
            constraints: A map of constraints, where a constraint is the fact
            that a certain parking place is reserved only for certain cars.
            position_empty: Target position (e.g., that of the empty slot).

        Returns:
            A set of cars that can be moved to position_empty.
        """
        if constraints is not None and position_empty in constraints:
            return constraints[position_empty] - {self.symbol_empty}
        else:
            return set(self.cars) - {self.symbol_empty}

    def _rearrange_feasible_cars(self, constraints, empty_position,
                                 target_state):
        """Generates cars feasible from the empty slot with the target car first.

        A simple heuristic to start generating paths with a smaller number of
        moves.

        Args:
            constraints: A map of constraints, where a constraint is the fact
            that a certain parking place is reserved only for certain cars.
            empty_position: Index of the empty slot in the current state.
            target_state: Targeted state (arrangement of cars).

        Yields:
            A car feasible from the empty position where the first element is
            the target car that must be in the empty slot (if possible).
        """
        target_car = target_state[empty_position]
        feasible_cars = self._get_feasible_cars(constraints, empty_position)
        if target_car in feasible_cars:
            yield target_car
        yield from (car for car in feasible_cars if car != target_car)

    def _update_displaced_cars(self, displaced_cars: Set[CarType],
                               empty_pos: int,
                               next_car: CarType,
                               target_state: "ParkingState") \
            -> Tuple[bool, bool]:
        """Checks how the state is changed by moving the car `next_car`.

        One move of a car can decrease the total number of incorrectly parked
        cars by 1 at the maximum, where incorrectly parked cars are those
        whose current position differs from the target one.
        There exist two cases:
            1) If the empty slot is not in the right place we can decrease
            count of incorrect cars by 1 (we can move the correct car to the
            empty place).
            2) If initially the empty slot is in the right place we cannot
            decrease the total number of incorrectly parked cars with a one
            move. The optimal move in this case is not to increase it (we
            can move an incorrect car to the empty place).
        Number of times when the empty slot will be on its right place equals
        to the number of cycles in the permutation.
        So, minimal count of movements = SUM (l_i + 1), where i from 1 to N,
        N is the count of permutation's cycles, l_i is a length of i-th cycle.

        Args:
            displaced_cars: A set of cars that are not in their right positions.
            empty_pos: Index of the currently empty slot.
            next_car: The car being moved.
            target_state: Targeted state (arrangement of cars).

        Returns:
            car_moved_to_target: True if the next car has been moved to its
            right place, False otherwise.
            car_was_in_target: True if the next car was already in its right
            slot and now is incorrectly placed, False otherwise.
        """
        car_was_in_target = \
            self._positions[next_car] == target_state._positions[next_car]
        car_moved_to_target = empty_pos == target_state._positions[next_car]
        if car_was_in_target:
            displaced_cars.add(next_car)
        elif car_moved_to_target:
            displaced_cars.remove(next_car)
        return car_moved_to_target, car_was_in_target

    def _restore_state(self, car_moved_to_target, car_was_in_target,
                       current_moves, displaced_cars, empty_position,
                       feasible_car):
        """Restores the state to the previous step while backtracking."""
        self._swap_cars_and_pos(self._positions[feasible_car],
                                empty_position)
        current_moves.pop()
        if car_was_in_target:
            displaced_cars.discard(feasible_car)
        elif car_moved_to_target:
            displaced_cars.add(feasible_car)

    def _swap_cars_and_pos(self, x_ind: int, y_ind: int) -> MoveType:
        """Swaps two elements at the given positions and returns that move."""
        self.cars[x_ind], self.cars[y_ind] = self.cars[y_ind], self.cars[x_ind]
        self._positions[self.cars[x_ind]], self._positions[self.cars[y_ind]] = (
            self._positions[self.cars[y_ind]],
            self._positions[self.cars[x_ind]])
        return MoveType(self.cars[y_ind], y_ind)
