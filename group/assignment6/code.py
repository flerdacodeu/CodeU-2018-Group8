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
from typing import List, Tuple, Generator, T

logging.basicConfig(filename="code.log", filemode='w', level=logging.DEBUG)

_MoveType = Tuple[int, int]


class Parking:
    """Data structure storing the start & end states, and the sequence of moves.

    Args:
        start: Start state.
        end: End state.
        empty: Representation of the empty slot.

    Attributes:
        self.start: start state.
        self.end: end state.
        self.n_cars: number of parking slots.
        self._incorrect_cars: set of numbers of cars that are on wrong places.
        self._current: current state.
        self._inverse_current: stores positions of each car.

    Raises:
        ValueError: Incorrect input.
    """

    def __init__(self, start: List[int], end: List[int], empty: T = 0):
        self._validate_input(start, end)

        self.start = start
        self.end = end
        self.n_cars = len(start)
        self.empty = empty

        self._incorrect_cars = {car for car, end_car in zip(start, end)
                                if car != end_car and car != empty}
        self._end_empty_position = self.end.index(self.empty) if end else None
        self._current = self.start.copy()
        self._inverse_current = {car: idx for idx, car in enumerate(start)}

        logging.debug(("start: ", self.start))
        logging.debug(("end: ", self.end))
        logging.debug(("incorrect cars: ", self._incorrect_cars))

    @staticmethod
    def _validate_input(start: List[int], end: List[int]):
        """Validates the input by checking type and value consistency."""
        if not type(start) == type(end) == list:
            raise ValueError("Incorrect input! start, end should be lists")
        if len(start) != len(end):
            raise ValueError(f"Incorrect input! len(start) {len(start)} != "
                             f"len(end) {len(end)}")
        if sorted(start) != sorted(end):
            raise ValueError("Incorrect input! Both start and end lists "
                             "should contain the same cars.")

    def get_moves(self) -> List[_MoveType]:
        """Computes a sequence of moves from the start state to the end state.

        Returns:
            A list of moves leading from the start state to the end state.
        """
        return list(self._get_moves())

    def _get_moves(self) -> Generator[_MoveType, None, None]:
        """Generates a sequence of moves from the start state to the end state.

        Yields:
            A car move (car, target position).
        """
        while self._incorrect_cars:
            # the empty slot is in the right place
            if self._inverse_current[self.empty] == self._end_empty_position:
                incorrect_car = self._incorrect_cars.pop()  # any car
                yield self._swap(incorrect_car)
                self._incorrect_cars.add(incorrect_car)
            # in the place of the empty slot should be another car
            incorrect_car = self.end[self._inverse_current[self.empty]]
            yield self._swap(incorrect_car)
            self._incorrect_cars.discard(incorrect_car)

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
