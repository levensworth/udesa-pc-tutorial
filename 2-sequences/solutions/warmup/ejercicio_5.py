import typing


from typing import List

def find_elemn(a_list: List, elem) -> bool:
    
    for e in a_list:
        if e == elem:
            return True
    return False

