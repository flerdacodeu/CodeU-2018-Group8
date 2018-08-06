# -*- coding: utf-8 -*-
"""Computes a sequence of moves from the start state to the target state.

Uses: 
    - Data structure which represents the start and target states which
support validation and swapping functionality (see class ParkingState);
    - Representation of the sequence of moves (List[MoveType]).

Computes:
1) Given target state, computes the shortest sequence of moves to obtain it.
2) Given target state and set of constraints, computes a sequence of moves 
which are inline with the given constraints.
3) Given target state, computes all the possible sequence of moves that lead 
from the start to the target state, without ever repeating the same 
configuration more than once.
"""

import copy
from typing import List, Set, Dict

from parking_state import ParkingState, CarType, MoveType


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

    def __init__(self, start: List[CarType], empty: CarType = 0,
                 constraints: Dict[int, Set[CarType]] = None):
        self.state = ParkingState(start, empty)
        if constraints is not None:
            self._validate_constraints(constraints)
        self.constraints = constraints
        self._seen_states = set()

    def __len__(self):
        return len(self.state)

    def get_moves(self, target_state: List[CarType],
                  retain_state: bool = False) -> List[MoveType]:
        """Computes a sequence of moves from the start state to the target one.

        Unless deselected, self.state is updated as the moves are generated,
        and finally set to target_state.

        Args:
            target_state: Targeted state (arrangement of cars).
            retain_state: Retains self.state unchanged if True,
            updates it as moves are generated if False.

        Returns:
            List of car moves (car, position) where car is any CarType object,
            and the latter is the position to which car should be moved.
        """
        state, target_state = self._prepare_states(retain_state, target_state)
        return next(state.generate_all_paths([], target_state,
                                             self._find_diff(target_state),
                                             self._seen_states,
                                             self.constraints),
                    None)

    def _prepare_states(self, retain_state, target_state):
        """Creates and validates the current and target ParkingState objects."""
        target_state = ParkingState(target_state, self.state.symbol_empty)
        self._validate_two_states(target_state)
        self._validate_feasibility(target_state)
        state = self.state if not retain_state else copy.deepcopy(self.state)
        return state, target_state

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
        state, target_state = self._prepare_states(retain_state, target_state)
        return sorted(
            state.generate_all_paths([], target_state,
                                     self._find_diff(target_state),
                                     self._seen_states, self.constraints),
            key=lambda path: len(path))

    def _validate_constraints(self, constraints: Dict[int, Set[CarType]]):
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

    def _find_diff(self, state: "ParkingState") -> Set[CarType]:
        """Returns elements of current state that differ from those of state."""
        self._validate_two_states(state)
        return {car for car, end_car in zip(self.state.cars, state.cars)
                if car != end_car and car != self.state.symbol_empty}

    def update_constraints(self, constraints: Dict[int, Set[CarType]]):
        """Adds/updates constraints to the current parking state."""
        if constraints is not None:
            self._validate_constraints(constraints)
        self.constraints = constraints
