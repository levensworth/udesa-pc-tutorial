from typing import List



def merge_sort(a_list: List[int]) -> list[int]:
    
    if len(a_list) == 0 or len(a_list) == 1:
        return a_list
    
    mid_idx = len(a_list)//2

    sorted_half = merge_sort(a_list[:mid_idx])
    sorted_half_2 = merge_sort(a_list[mid_idx:])

    ord_list = merge_lists(sorted_half, sorted_half_2)
    return ord_list
    


def merge_lists(a_list: List[int], b_list: List[int]) -> List[int]:

    result = []
    
    idx_a = 0
    idx_b = 0

    while idx_a < len(a_list) and idx_b < len(b_list):

        if a_list[idx_a] > b_list[idx_b]:
            result.append(b_list[idx_b])
            idx_b += 1

        elif a_list[idx_a] < b_list[idx_b]:
            result.append(a_list[idx_a])
            idx_a += 1

        else:
            result.append(a_list[idx_a])
            result.append(b_list[idx_b])
            idx_a += 1
            idx_b += 1

    
    result += a_list[idx_a:]

    result += b_list[idx_b:]

    return result


print(merge_sort([6,5,4]))