# -*- coding: utf-8 -*-
"""Computes a sequence of moves from the start state to the end state.

Fewer moves:
    We can't decrease the count of incorrectly parked cars by more
    than 1 for one movement.
    If initially the empty slot is in the right place we can't decrease
    count of incorrect cars, so we shouldn't increase it
    (we can move any incorrect car to empty place).
    If the empty slot is not in the right place we can decrease
    count of incorrect cars by 1 (we can move correct car to empty place).
    Number of times when the empty slot will be on its right place equals
    to the number of cycles in the permutation.
    So, minimal count of movements = SUM (l_i + 1), where i from 1 to N,
    N is the count of permutation's cycles, l_i is a length of i-th cycle.
"""

import copy
import logging
from typing import List, Tuple, Set, Dict, Hashable

logging.basicConfig(filename="parking.log", filemode="w", level=logging.DEBUG)

_CarType = Hashable
_MoveType = Tuple[_CarType, _CarType]


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

    def __len__(self):
        return len(self.cars)

    def _swap(self, x_ind: int, y_ind: int = None):
        """Swaps two elements of the list at the positions x_ind and y_ind."""
        y_ind = y_ind or self._get_position_empty()
        self.cars[x_ind], self.cars[y_ind] = self.cars[y_ind], self.cars[x_ind]

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

    def _validate_two_states(self, state: "ParkingState"):
        if len(self.cars) != len(state):
            raise ValueError(
                f"States' lengths mismatch, {len(self)} != {len(state)}")
        if self.symbol_empty != state.symbol_empty:
            raise ValueError(
                f"The two states have different empty slot symbols: "
                f"{self.symbol_empty} & {state.symbol_empty}.")
        if set(self.get()) != set(state.get()):
            raise ValueError(
                "The two sets of cars are different. Cannot find moves.")

    def _find_diff(self, state: "ParkingState") -> Set[_CarType]:
        """Returns elements of current state that differ from those of state."""
        self._validate_two_states(state)
        return {car for car, end_car in zip(self.cars, state.get())
                if car != end_car and car != self.symbol_empty}

    def _get_feasible_cars(self, constraints: Dict[int, Set[_CarType]],
                           position_empty: int) -> Set[_CarType]:
        """Returns set of cars that can be moved to position_empty.

        Args:
            constraints: A set of constraints, where a constraint is the fact
            that a certain parking place is reserved only for certain cars.
            position_empty: Target position (e.g., that of the empty slot).

        Returns:
            A set of cars that can be moved to position_empty.
        """
        if constraints is not None and position_empty in constraints:
            cars = set(constraints[position_empty])
        else:
            cars = set(self.get())
        return cars - {self.symbol_empty}

    def _get_next_move(self, target_state: "ParkingState",
                       constraints: Dict[int, Set[_CarType]] = None):
        """#todo: doc

        Args:
            target_state:
            constraints:

        Returns:

        """
        displaced_cars = self._find_diff(target_state)
        logging.debug(("displaced cars: ", displaced_cars))
        positions = self._get_positions()
        target_empty_position = target_state._get_position_empty()
        flag_random = False  # quick "fix"

        while displaced_cars:
            position_empty = positions[self.symbol_empty]
            if flag_random:  # todo: remove this branch when fixed
                car = self._get_feasible_cars(constraints,
                                              position_empty).pop()
                flag_random = False
            elif position_empty == target_empty_position:
                feasible_cars = self._get_feasible_cars(constraints,
                                                        position_empty)
                intersection = displaced_cars & feasible_cars
                if not intersection:
                    car = feasible_cars.pop()
                    displaced_cars.add(car)
                    flag_random = True
                else:
                    car = intersection.pop()
            else:
                car = target_state.get()[position_empty]
                displaced_cars.discard(car)

            self._swap(positions[car], position_empty)
            positions[car], positions[self.symbol_empty] = (position_empty,
                                                            positions[car])
            logging.debug((car, " -> 0", positions[car], displaced_cars))
            yield car, positions[car]

    def get(self):
        return self.cars

    def _get_position_empty(self):
        return self._get_positions()[self.symbol_empty] if len(
            self) > 0 else None

    def _get_positions(self):
        return {x: index for index, x in enumerate(self.cars)}


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
                 constraints: Dict[_CarType, Set[_CarType]] = None):
        self.state = ParkingState(start, empty)
        if constraints is not None:
            self._validate_constraints(constraints)
        self.constraints = constraints

    def __len__(self):
        return len(self.state)

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
            if len(cars & set(self.get_state())) != len(cars):
                raise ValueError("Unrecognized vehicle(s).")

            constraints[position].add(self.state.symbol_empty)

    def get_moves(self, target_state: List[_CarType],
                  retain_state: bool = False) -> List[_MoveType]:
        """
        Computes a sequence of moves from the start state to the given
        target state. Unless deselected, self.state is updated as the
        moves are generated, and finally set to target_state.
        :param target_state: [list of _CarType objects] targeted state
        :param retain_state: [bool] retains self.state unchanged if True,
         updates it as moves are generated if False
        :return: [list of tuples (car, int)] where car is any _CarType object,
        and the latter is the position to which car should be moved
        """
        target_state = ParkingState(target_state,
                                    self.state.symbol_empty)
        self.state._validate_two_states(target_state)
        self._validate_feasibility(target_state)

        current_state = self.state if not retain_state else copy.deepcopy(
            self.state)

        logging.debug(("start: ", self.state.get()))
        logging.debug(("end: ", target_state.get()))

        return list(
            current_state._get_next_move(target_state, self.constraints))

    def get_state(self):
        """Returns the current state of the parking lot."""
        return self.state.get()

    def update_constraints(self, constraints: Dict[int, Set[_CarType]]):
        """Adds/updates constraints to the current parking state."""
        if constraints is not None:
            self._validate_constraints(constraints)
        self.constraints = constraints

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
        for pos, car in enumerate(target_state.get()):
            if pos in self.constraints and car not in self.constraints[pos]:
                raise ValueError(
                    "Found contradiction between constraints and target state.")
