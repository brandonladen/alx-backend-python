#!/usr/bin/env python3
'''
A model for complex types-mixed list
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    total: float = 0.0
    for num in mxd_lst:
        total += num

    return total
