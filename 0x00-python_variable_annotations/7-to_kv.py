#!/usr/bin/env python3
'''
Module for complex types - string and int/float to tuple
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''returns a tuple'''
    return (k, v*v)
