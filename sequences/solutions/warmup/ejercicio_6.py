from typing import List 

def remove_duplicates(a_list: List) -> List:
    """
    Given a list with duplicate elements, remove duplicates. It uses the __eq__ 
    protocol for comparison
    Parasm:
    a_list: List of elements.

    Returns:
    a list of unique elements.
    """
    new_list = []

    for elem in a_list:
        if elem not in new_list:
            new_list.append(elem)

    return new_list


def remove_duplicates_2(a_list: List) -> List:
    new_list = []
    for elem in a_list:
        if not find_elem(new_list, elem):
            new_list.append(elem)
    
    return new_list

def find_elem(list: List, elem) -> bool:
    for i in list:
        if i == elem:
            return True
    return False
    


