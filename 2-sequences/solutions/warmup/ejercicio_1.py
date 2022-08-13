
from typing import List


def filter_even(a_list: List) -> List:
    """
    Given a list of integers, return a new list of only even elements.
    Params:
        - a_list: list of Integers
    Returns:
        a new list of even elements from the original list.
    """
    result = []
    for elem in a_list:
        if elem % 2 == 0:
            result.append(elem)
    
    return result
