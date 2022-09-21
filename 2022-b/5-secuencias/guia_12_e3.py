from ctypes import Union
from typing import Callable, List



def has_enough_length(string: str) -> bool:
    return len(string) >= 8 and len(string) <= 31


def contains_upper(string: str) -> bool:
    for c in string:
        is_cap = ord(c) >= ord('A') and ord(c) <= ord('Z')
        if not is_cap:
            return False

    return True


def verify_str(string: str, constraints: List[Callable[[str], bool]]) -> bool:
    '''
    Verify if a given string actually complies with the given contraints.

    Args:
    - string: (str) is the string to evaluate.
    - constraints: (list of functional predicates) is a list 
        of funcitions which should expect a string as argument and return bool.
    
    Returns: True if the string complies, False if not.
    '''
    
    for const in constraints:
        if not const(string):
            return False
        
    return True




def main():
    user_input = 'password'

    constraints = [has_enough_length, contains_upper]
    if verify_str(user_input, constraints):
        print('ta todo ok')

    else:
        print('no ta ok')



if __name__ == '__main__':
    main()