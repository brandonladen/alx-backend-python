#!/usr/bin/env python3
'''
A module for complex types-functions
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''returns a function'''
    def mult(x: float) -> float:
        '''returns a float'''
        return multiplier * x
    return mult
