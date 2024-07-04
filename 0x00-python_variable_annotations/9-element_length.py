#!/usr/bin/env python3
'''
Model for duck type object
'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''returns tuple in a list'''
    return [(i, len(i)) for i in lst]
