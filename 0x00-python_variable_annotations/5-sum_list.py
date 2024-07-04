#!/usr/bin/env python3
'''
Module for complex type-list of floats
'''


from typing import List


def sum_list(input_list: List[float]) -> float:
    '''returns float'''
    total: float = 0.0
    for num in input_list:
        total += num
    return total
