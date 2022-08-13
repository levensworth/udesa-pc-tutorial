from typing import List

def merge_lists(a_list: List, b_list: List) -> List:
    
    a_idx = 0
    b_idx = 0

    result = []

    while a_idx < len(a_list) and b_idx < len(b_list):
        # decide which to inlcude and append value
        # increment counter acordingly
        
        result.append(min(a_list[a_idx], b_list[b_idx]))
        a_idx, b_idx = update_counters(a_list, b_list, a_idx, b_idx)

    
    # At this point, one of the 2 lists is empty
    
    while a_idx < len(a_list):
        result.append(a_list[a_idx])
        a_idx += 1

    
    while b_idx < len(b_list):
        result.append(b_list[b_idx])
        b_idx += 1
    
    return result


def update_counters(a_list: List, b_list: List, a_idx: int, b_idx: int):
    if a_list[a_idx] < b_list[b_idx]:
        a_idx += 1

    elif a_list[a_idx] > b_list[b_idx]:
        b_idx +=1 
    
    else:
        a_idx += 1
        b_idx += 1

    return a_idx, b_idx

        

print(merge_lists([1,4,6,11], [2]))