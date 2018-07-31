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
import copy
from typing import List, Tuple, Generator, TypeVar

logging.basicConfig(filename="parking.log", filemode='w', level=logging.DEBUG)

T = TypeVar('T')
_MoveType = Tuple[int, int]


class ParkingState:
    """
    Implements a wrapper of a list which represents the state of the parking lot.
    The state list is of length N, its indices are the N parking slots,
    and its elements are the N-1 cars and the empty slot.
    The cars/empty_slot_symbol could be any hashable object.
    """

    def __init__(self, input_list, empty_slot=0):
        self._validate_state(input_list, empty_slot)
        self.cars = input_list
        self.symbol_empty = empty_slot

    def swap(self, x_ind, y_ind=None):
        y_ind = y_ind or self.get_position_empty()
        self.cars[x_ind], self.cars[y_ind] = self.cars[y_ind], self.cars[x_ind]

    @staticmethod
    def _validate_state(state, symbol_empty):
        """
        Validates if technical and parking lot state properties hold for the input.
        This includes:
            1) input must be list;
            2) input contains no duplicates;
            3) given the empty slot representation, the input list contains exactly one empty slot
        Raises:
            TypeError: property 1 violated.
            ValueError: property 2 or 3 violated.
            
        :param state: [list] list of cars, where car is any hashable object 
        :param symbol_empty: [hashable object] symbol of the empty slot
        :return: [None] 
        """
        if not isinstance(state, list):
            raise TypeError("Unsupported operand type: " + type(state))

        if len(state) > 0 and state.count(symbol_empty) != 1:
            raise ValueError('Invalid input, expected one empty slot.')

        if len(state) != len(set(state)):
            raise ValueError('Invalid input: duplicate element(s) found.')

    def _validate_two_states(self, state):
        if len(self.cars) != len(state):
            raise ValueError(f"States' lengths mismatch, {len(self)} != {len(state)}")
        if self.get_symbol_empty() != state.get_symbol_empty():
            raise ValueError(f"The two states have different empty slot symbols: "
                             f"{self.get_symbol_empty()} & {state.get_symbol_empty()}.")
        if set(self.get()) != set(state.get()):
            raise ValueError("The two sets of cars are different. Cannot find moves.")

    def compare(self, state):
        """
        Returns elements of current state that differ from those of state.
        :param state: [ParkingState] instance of State
        :return: [set of objects] the different elements of self.cars
        """
        self._validate_two_states(state)
        return {car for car, end_car in zip(self.cars, state.get())
                if car != end_car and car != self.symbol_empty}

    def get_feasible_cars(self, constraints, _position_empty):
        """
        Returns set of cars that can be moved to position_empty
        :param constraints: 
        :param position_empty: 
        :return: [set]
        """
        if constraints is not None and _position_empty in constraints:
            _cars = set(constraints[_position_empty])
        else:
            _cars = set(self.get())
        return _cars - set([self.symbol_empty])

    def get_next_move(self, target_state, constraints=None):
        _displaced_cars = self.compare(target_state)
        logging.debug(("displaced cars: ", _displaced_cars))
        _positions = self.get_positions()
        _target_empty_position = target_state.get_position_empty()
        _flag_random = False  # quick 'fix'

        while _displaced_cars:
            _position_empty = _positions[self.symbol_empty]
            if _flag_random:  # todo: remove this branch when fixed
                _car = self.get_feasible_cars(constraints, _position_empty).pop()
                _flag_random = False
            elif _position_empty == _target_empty_position:
                _feasible_cars = self.get_feasible_cars(constraints, _position_empty)
                _intersection = _displaced_cars & _feasible_cars
                if len(_intersection) == 0:
                    _car = _feasible_cars.pop()
                    _displaced_cars.add(_car)
                    _flag_random = True
                else:
                    _car = _intersection.pop()
            else:
                _car = target_state.get()[_position_empty]
                _displaced_cars.discard(_car)

            # Swap: _car & _empty
            self.swap(_positions[_car], _position_empty)
            _positions[_car], _positions[self.symbol_empty] = _position_empty, _positions[_car]
            logging.debug((_car, " -> 0", _positions[_car], _displaced_cars))
            yield _car, _positions[_car]

    def __len__(self):
        return len(self.cars)

    def get(self):
        return self.cars

    def get_symbol_empty(self):
        return self.symbol_empty

    def get_position_empty(self):
        return self.get_positions()[self.symbol_empty] if len(self) > 0 else None

    def get_positions(self):
        return {x: index for index, x in enumerate(self.cars)}


class ParkingLot:
    """
    Implements a ParkingLot of N slots and N-1 cars in it. 
    Each instance stores the current state (see class ParkingState) 
    as well as a set of constraints, where a constraint is indicating
    that a certain parking place is reserved only for certain cars. 
    """

    def __init__(self, start: List[int], empty: T = 0, constraints=None):
        """
        
        :param start: [list of hashable objects] ordered list of cars/empty slot
        :param empty: [hashable object] object representing the empty slot, used in start
        :param constraints: [dict] of <int, set> pairs, denoting <positions, allowed_cars>
        
        Raises:
            TypeError & ValueError, see ParkingState._validate()
        """
        self.state = ParkingState(start, empty)
        if constraints is not None:
            self._validate_constraints(constraints)
        self.constraints = constraints

    def __len__(self):
        """
        Returns the total number N of slots in the parking.
        :return: [int]
        """
        return len(self.state)

    def get_moves(self, target_state, retain_state=False):
        """
        Computes a sequence of moves from the start state to the given 
        target state. Unless deselected, self.state is updated as the
        moves are generated, and finally set to target_state.
        :param target_state: [list of hashable objects] targeted state
        :param retain_state: [bool] retains self.state unchanged if True,
         updates it as moves are generated if False
        :return: [list of tuples (car, int)] where car is any hashable object, 
        and the latter is the position to which car should be moved
        """
        target_state = ParkingState(target_state, self.state.get_symbol_empty())
        self.state._validate_two_states(target_state)
        self._validate_feasibility(target_state)

        _current_state = self.state if not retain_state else copy.deepcopy(self.state)

        logging.debug(("start: ", self.state.get()))
        logging.debug(("end: ", target_state.get()))

        return list(_current_state.get_next_move(target_state, self.constraints))

    def get_state(self):
        """
        Returns the current state of the parking lot.
        :return: [list of hashable objects]
        """
        return self.state.get()

    def _validate_constraints(self, constraints):
        """
        The given conditions:
            1) must be dictionary of < int, set > pairs;
            2) each key must be in [0, N); and
            3) each element in the set must be element of self.cars.
            
        Note: 'position not in constraints', implies any car can park at it.
        Note: As any parking slot can be free, it adds the empty slot to the set.
        
        Raises:
            TypeError: property 1 violated.
            ValueError: property 2 or 3 violated.

        :param constraints: [dict] of <int, set> pairs, denoting <positions, allowed_cars>
        :return: [None]
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
                raise ValueError(f"Out of bounds. {position} not in [0, {len(self)}]")

            if len(cars & set(self.get_state())) != len(cars):
                raise ValueError('Unrecognized vehicle(s).')

            constraints[position].add(self.state.get_symbol_empty())

    def update_constraints(self, constraints):
        if constraints is not None:
            self._validate_constraints(constraints)
        self.constraints = constraints

    def _validate_feasibility(self, target_state):
        """
        Checks for contradiction between the constraints and the target state.
        
        Raises:
            ValueError
        :param target_state: [ParkingState]
        :return: [None]
        """
        if self.constraints is None:
            return
        for position, car in enumerate(target_state.get()):
            if position in self.constraints and car not in self.constraints[position]:
                raise ValueError('Found contradiction between constraints and target state.')
