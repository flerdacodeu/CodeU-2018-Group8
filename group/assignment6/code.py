# -*- coding: utf-8 -*-
"""Computes a sequence of moves from the start state to the end state.

Data structure which represents start and end states:
    For each state it stores two lists: state and inverse_state;
    state: stores number of cars for each place,
    the empty slot is represented as 0;
    inverse_state: stores number of the parking place for each car.

    It stores 3 types of states: start state,
    end state and current state (after some moves).

    Also it stores set of cars that are parked on wrong places.

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

import logging
from typing import List, Tuple, Generator, TypeVar

logging.basicConfig(filename="code.log", filemode='w', level=logging.DEBUG)

T = TypeVar('T')
_MoveType = Tuple[int, int]


class Parking:
    """Data structure storing the start & end states, and the sequence of moves.

    Args:
        start: Start state.
        end: End state.
        empty: Representation of the empty slot.

    Attributes:
        self.start: Start state.
        self.end: End state.
        self._displaced_cars: Set of car ids that are in wrong places.
        self._current: Current state.
        self._inverse_current: Map storing positions of each car.

    Raises:
        ValueError: Invalid input.
    """

    def __init__(self, start: List[int], end: List[int], empty: T = 0):
        self._validate_input(start, end, empty)

        self.start = start
        self.end = end
        self.empty = empty

        self._displaced_cars = {car for car, end_car in zip(start, end)
                                if car != end_car and car != empty}
        self._end_empty_position = self.end.index(self.empty) if end else None
        self._current = self.start.copy()
        self._inverse_current = {car: idx for idx, car in enumerate(start)}

        logging.debug(("start: ", self.start))
        logging.debug(("end: ", self.end))
        logging.debug(("displaced cars: ", self._displaced_cars))

    def __len__(self):
        return len(self.start)

    @staticmethod
    def _validate_input(start: List[int], end: List[int], empty: T):
        """Validates the input by checking type and value consistency."""
        if not isinstance(start, list) or not isinstance(end, list):
            raise TypeError("Incorrect input! start, end should be lists")
        if len(start) != len(end):
            raise ValueError(f"Incorrect input! len(start) {len(start)} != "
                             f"len(end) {len(end)}")
        if set(start) != set(end):
            raise ValueError("Incorrect input! Both start and end lists "
                             "should contain the same cars.")
        if len(start) > 0 and start.count(empty) != 1:
            raise ValueError('Invalid input: expected one empty slot.')

    def get_moves(self) -> List[_MoveType]:
        """Computes a sequence of moves from the start state to the end state.

        Returns:
            A list of moves leading from the start state to the end state.
        """
        return list(self._get_optimal_moves())

    def _get_optimal_moves(self) -> Generator[_MoveType, None, None]:
        """Generates a sequence of moves from the start state to the end state.

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

        Yields:
            A car move (car, target position).
        """
        while self._displaced_cars:
            # the empty slot is in the right place
            if self._inverse_current[self.empty] == self._end_empty_position:
                displaced_car = self._displaced_cars.pop()  # any car
                yield self._swap(displaced_car)
                self._displaced_cars.add(displaced_car)
            # in the place of the empty slot should be another car
            displaced_car = self.end[self._inverse_current[self.empty]]
            yield self._swap(displaced_car)
            self._displaced_cars.discard(displaced_car)

    def _swap(self, x: int) -> _MoveType:
        """Moves the car #x to the empty slot.

        Args:
            x: The number of a car.

        Returns:
            A car move (car, target position).
        """
        self._inverse_current[x], self._inverse_current[self.empty] = (
            self._inverse_current[self.empty], self._inverse_current[x])
        self._current[self._inverse_current[self.empty]] = self.empty
        self._current[self._inverse_current[x]] = x
        logging.debug((x, " -> 0", self._current))
        return x, self._inverse_current[x]
