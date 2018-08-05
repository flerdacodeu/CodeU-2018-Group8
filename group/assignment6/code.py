# -*- coding: utf-8 -*-
"""Computes a sequence of moves from the start state to the end state.

1) Defines a data structure to represent the start and end states (ParkingState)
and the sequence of moves (List[_MoveType]).
2) Computes the sequence of moves to go from the start to the end state with
fewer moves.
3) Computes a sequence of moves that enforces a set of constraints.
4) Computes all the possible sequence of moves that lead from the start to
the end state without ever repeating the same configuration more than once.
"""

import copy
from typing import List, Set, Dict, Hashable, NamedTuple, Generator, Tuple

_CarType = Hashable
_MoveType = NamedTuple("_MoveType", [("car", "_CarType"), ("to", int)])


class ParkingState:
    """Implements a wrapper of a list representing the state of a parking lot.

    Attributes:
        cars: The state list of length N, its indices are the N parking slots,
        and its elements are the N-1 cars and the empty slot.
        symbol_empty: A symbol representing the empty slot, any _CarType object.
    """

    def __init__(self, input_list: List[_CarType], empty_slot: _CarType = 0):
        self._validate_state(input_list, empty_slot)
        self.cars = input_list
        self.symbol_empty = empty_slot
        self._positions = {car: index for index, car in enumerate(self.cars)}

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, idx):
        return self.cars[idx]

    @staticmethod
    def _validate_state(state: List[_CarType], symbol_empty: _CarType):
        """Validates if technical and parking state properties hold for input.

        This includes:
            1) input must be list;
            2) input contains no duplicates;
            3) given the empty slot representation, the input list contains
            exactly one empty slot.

        Args:
            state: List of cars, where car is any _CarType object.
            symbol_empty: Symbol of the empty slot.

        Raises:
            TypeError: Property 1 violated.
            ValueError: Property 2 or 3 violated.
        """
        if not isinstance(state, list):
            raise TypeError(f"Unsupported operand type: {type(state)}")

        if len(state) > 0 and state.count(symbol_empty) != 1:
            raise ValueError("Invalid input, expected one empty slot.")

        if len(state) != len(set(state)):
            raise ValueError("Invalid input: duplicate element(s) found.")

    def generate_all_paths(self, current_moves: List[_MoveType],
                           target_state: "ParkingState",
                           displaced_cars: Set[_CarType], seen_states,
                           constraints: Dict[int, Set[_CarType]]) \
            -> Generator[List[_MoveType], None, None]:
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

    def _get_feasible_cars(self, constraints: Dict[int, Set[_CarType]],
                           position_empty: int) -> Set[_CarType]:
        """Returns the set of cars that can be moved to position_empty.

        Args:
            constraints: A map of constraints, where a constraint is the fact
            that a certain parking place is reserved only for certain cars.
            position_empty: Target position (e.g., that of the empty slot).

        Returns:
            A set of cars that can be moved to position_empty.
        """
        if constraints is not None and position_empty in constraints:
            return set(constraints[position_empty]) - {self.symbol_empty}
        else:
            return set(self.cars) - {self.symbol_empty}

    def _rearrange_feasible_cars(self, constraints, empty_position,
                                 target_state):
        """Puts the target car that needs to be in the empty position to idx 0.

        A simple heuristic to start generating paths with a smaller number of
        moves.

        Args:
            constraints: A map of constraints, where a constraint is the fact
            that a certain parking place is reserved only for certain cars.
            empty_position: Index of the empty slot in the current state.
            target_state: Targeted state (arrangement of cars).

        Returns:
            Rearranged list of cars feasible from the empty position where
            the first element is the target car that must be in the empty slot
            (if possible).
        """
        feasible_cars = list(
            self._get_feasible_cars(constraints, empty_position))
        for idx, car in enumerate(feasible_cars):
            if car == target_state[empty_position]:
                feasible_cars[0], feasible_cars[idx] = (feasible_cars[idx],
                                                        feasible_cars[0])
                break
        return feasible_cars

    def _update_displaced_cars(self, displaced_cars: Set[_CarType],
                               empty_pos: int,
                               next_car: _CarType,
                               target_state: "ParkingState") \
            -> Tuple[bool, bool]:
        """Checks how the state is changed by moving the car `next_car`.

        We can't decrease the count of incorrectly parked cars by more
        than 1 for one movement.
        If the empty slot is not in the right place we can decrease
        count of incorrect cars by 1 (we can move correct car to empty place).
        If initially the empty slot is in the right place we can neither
        decrease not increase the count of incorrect cars
        (we can move any incorrect car to empty place).
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

    def _swap_cars_and_pos(self, x_ind: int, y_ind: int) -> _MoveType:
        """Swaps two elements at the given positions and returns that move."""
        self.cars[x_ind], self.cars[y_ind] = self.cars[y_ind], self.cars[x_ind]
        self._positions[self.cars[x_ind]], self._positions[self.cars[y_ind]] = (
            self._positions[self.cars[y_ind]],
            self._positions[self.cars[x_ind]])
        return _MoveType(self.cars[y_ind], y_ind)


class ParkingLot:
    """Implements a ParkingLot of N slots and N-1 cars in it.

    Each instance stores the current state (see class ParkingState)
    as well as a set of constraints, where a constraint is indicating
    that a certain parking place is reserved only for certain cars.

    Attributes:
        start: Ordered list of cars/empty slot.
        empty: Object representing the empty slot, used in start.
        constraints: A map of <position, allowed cars for the position>.

    Raises:
        TypeError, ValueError: See input validation in the ParkingState class.
    """

    def __init__(self, start: List[_CarType], empty: _CarType = 0,
                 constraints: Dict[int, Set[_CarType]] = None):
        self.state = ParkingState(start, empty)
        if constraints is not None:
            self._validate_constraints(constraints)
        self.constraints = constraints
        self._seen_states = set()

    def __len__(self):
        return len(self.state)

    def get_moves(self, target_state: List[_CarType],
                  retain_state: bool = False) -> List[_MoveType]:
        """Computes a sequence of moves from the start state to the target one.

        Unless deselected, self.state is updated as the moves are generated,
        and finally set to target_state.

        Args:
            target_state: Targeted state (arrangement of cars).
            retain_state: Retains self.state unchanged if True,
            updates it as moves are generated if False.

        Returns:
            List of car moves (car, position) where car is any _CarType object,
            and the latter is the position to which car should be moved.
        """
        target_state = ParkingState(target_state,
                                    self.state.symbol_empty)
        self._validate_two_states(target_state)
        self._validate_feasibility(target_state)
        displaced_cars = self._find_diff(target_state)
        current_state = self.state if not retain_state else copy.deepcopy(
            self.state)
        return next(current_state.generate_all_paths([], target_state,
                                                     displaced_cars,
                                                     self._seen_states,
                                                     self.constraints),
                    None)

    def get_all_paths(self, target_state, retain_state=False):
        """Computes all possible paths leading from the state to the target state.

        It does not have a single sequence that has the same parking lot
        configuration (positions of cars in the parking lot) more than once,
        however, different paths can share the same state.

        Args:
            target_state: Targeted state (arrangement of cars).
            retain_state: Retains self.state unchanged if True,
            updates it as moves are generated if False.

        Returns:
            A list of all possible paths leading from the start state to the
            target state, sorted by length (shortest first).
        """
        target_state = ParkingState(target_state,
                                    self.state.symbol_empty)
        self._validate_two_states(target_state)
        self._validate_feasibility(target_state)
        displaced_cars = self._find_diff(target_state)
        current_state = copy.deepcopy(
            self.state) if retain_state else self.state
        return sorted(
            current_state.generate_all_paths([], target_state, displaced_cars,
                                             self._seen_states,
                                             self.constraints),
            key=lambda path: len(path))

    def _validate_constraints(self, constraints: Dict[int, Set[_CarType]]):
        """Validates if constraints are applicable to the input.

        The given conditions:
            1) must be dictionary of < int, set > pairs;
            2) each key must be in [0, N); and
            3) each element in the set must be element of self.cars.

        Note: "Position not in constraints", implies any car can park at it.
        As any parking slot can be free, it adds the empty slot to the set.

        Raises:
            TypeError: Property 1 violated.
            ValueError: Property 2 or 3 violated.
        """
        if not isinstance(constraints, dict):
            raise TypeError(f"Unsupported type: {type(constraints)}. "
                            f"Expected dictionary.")

        for position, cars in constraints.items():
            if not isinstance(position, int):
                raise TypeError(f"Unsupported position type: {type(position)}. "
                                f"Expected int.")
            if not isinstance(cars, set):
                raise TypeError(f"Unsupported cars type: {type(cars)}. "
                                f"Expected set.")
            if not 0 <= position <= len(self):
                raise ValueError(
                    f"Out of bounds. {position} not in [0, {len(self)}]")
            if len(cars & set(self.state.cars)) != len(cars):
                raise ValueError("Unrecognized vehicle(s).")

            constraints[position].add(self.state.symbol_empty)

    def _validate_two_states(self, state: "ParkingState"):
        """Validates if the current state can be led to the target state."""
        if len(self.state.cars) != len(state):
            raise ValueError(
                f"States' lengths mismatch, {len(self.state)} != {len(state)}")
        if self.state.symbol_empty != state.symbol_empty:
            raise ValueError(
                f"The two states have different empty slot symbols: "
                f"{self.state.symbol_empty} & {state.symbol_empty}.")
        if set(self.state.cars) != set(state.cars):
            raise ValueError(
                "The two sets of cars are different. Cannot find moves.")

    def _validate_feasibility(self, target_state: ParkingState):
        """Checks for contradiction between constraints and the target state.

        Args:
            target_state: A ParkingState instance.

        Raises:
            ValueError: If there is a contradiction between constraints
            and target state.
        """
        if self.constraints is None:
            return
        for pos, car in enumerate(target_state.cars):
            if pos in self.constraints and car not in self.constraints[pos]:
                raise ValueError(
                    "Found contradiction between constraints and target state.")

    def _find_diff(self, state: "ParkingState") -> Set[_CarType]:
        """Returns elements of current state that differ from those of state."""
        self._validate_two_states(state)
        return {car for car, end_car in zip(self.state.cars, state.cars)
                if car != end_car and car != self.state.symbol_empty}

    def update_constraints(self, constraints: Dict[int, Set[_CarType]]):
        """Adds/updates constraints to the current parking state."""
        if constraints is not None:
            self._validate_constraints(constraints)
        self.constraints = constraints
