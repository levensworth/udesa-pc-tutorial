

from typing import List

'''
It should be noticed, that this function is a generalization of the prev problem.
Often, a generalization means transforming a hardcoded value or logic into a parameter of the function.
'''

def filter_multiples_of_n(a_list: List, n: int) -> List:
    """
    Given a list of integers, return a new list of only multiples of N elements.
    Params:
        - a_list: list of Integers
    Returns:
        a new list of elements multiples of N from the original list.
    """
    result = []
    for elem in a_list:
        if elem % n == 0:
            result.append(elem)
    
    return result



    

