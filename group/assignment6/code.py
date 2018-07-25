# -*- coding: utf-8 -*-
import logging
logging.basicConfig(filename="code.log", filemode='w', level=logging.DEBUG)

"""Computes sequence of moves from the start state to the end state.

Data structure to represent start and end states:
    For each state it stores two lists: state and inverse_state;
    state: stores number of cars for each place, 
    the empty slot is represented as 0;
    inverse_state: stores number of parking place for each car.
    
    It stores 3 types of states: start state,
    end state and current state (after some moves).
    
    Also it stores set of car that are on wrong places.

Fewer moves:
    We can't decrease count of incorrect cars by more than 1 for one movement.
    If initially the empty slot is on the right place we can't decrease
    count of incorrect cars, so we shouldn't increase it 
    (we can move any incorrect car to empty place).
    If the empty slot is not on the right place we can decrease 
    count of incorrect cars by 1 (we can move correct car to empty place).
    Empty slot will be on it's right place the number of cycles times.
    So, minimal count of movements = SUM (l_i + 1), where i from 1 to N, 
    N is count of permutation's cycles, l_i is a length of cycle.    
"""


class Parking:
    """Data structure to represent the start and end states
        and the sequence of moves. The empty slot is represented as 0.

    Attributes:
        self.start: start state.
        self.inverse_start: stores places of each car
            and empty slot for the start state.
        self.end: end state.
        self.inverse_end: stores places of each car
            and empty slot for the end state.
        self.n: size of parking.
        self.incorrect_cars: set of numbers of cars that are on wrong places.
        self.current, self.inverse_current: current state (after some moves).
    """
    def __init__(self, start, end):
        """
        Args:
            start: start state. List, permutation of numbers
            from 0 to size of parking.
            end: end state. List, permutation of numbers
            from 0 to size of parking.

        Raises:
            ValueError: incorrect input.
        """
        self.start = start
        self.end = end

        if not type(start) == type(end) == list:
            raise ValueError("Incorrect input! start, end should be lists")
        if len(start) != len(end):
            raise ValueError("Incorrect input! len(start) != len(end)")
        self.n = len(start)
        if not sorted(start) == sorted(end) == list(range(self.n)):
            raise ValueError("Incorrect input! start and end lists \
            should store all values from 0 to n-1.")
        self.incorrect_cars = {self.start[i]
                               for i in range(0, self.n)
                               if self.start[i] != self.end[i]}
        self.incorrect_cars.discard(0)
        self.inverse_start = [0] * self.n
        self.inverse_end = [0] * self.n
        for i in range(self.n):
            self.inverse_start[self.start[i]] = i
            self.inverse_end[self.end[i]] = i
        self.current = self.start.copy()
        self.inverse_current = self.inverse_start.copy()
        logging.debug(("start: ", self.start))
        logging.debug(("inv_start: ", self.inverse_start))
        logging.debug(("end: ", self.end))
        logging.debug(("inv_end: ", self.inverse_end))
        logging.debug(("incorrect cars: ", self.incorrect_cars))

    def _swap(self, x):
        """Moves car #x to empty slot.

        Args:
            x: number of car.

        Returns:
            move: pair (car, target position).
        """
        self.inverse_current[x], self.inverse_current[0] = \
            self.inverse_current[0], self.inverse_current[x]
        self.current[self.inverse_current[0]] = 0
        self.current[self.inverse_current[x]] = x
        logging.debug((x, " -> 0", self.current))
        return x, self.inverse_current[x]

    def get_moves(self):
        """Computes sequence of moves from the start state to the end state.

        Returns:
            sequence: list of pairs (car, target position).
        """
        sequence = []
        while self.incorrect_cars:
            # the empty slot on the right place
            if self.inverse_current[0] == self.inverse_end[0]:
                # any car
                x = self.incorrect_cars.pop()
                sequence.append(self._swap(x))
                self.incorrect_cars.add(x)
            # on the place of the empty slot should be another car
            x = self.end[self.inverse_current[0]]
            sequence.append(self._swap(x))
            self.incorrect_cars.discard(x)
        return sequence
