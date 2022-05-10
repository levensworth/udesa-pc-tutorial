from typing import List


from typing import List

def zip_lists(l1:List, l2: List) -> List:
    result = []
    
    for idx, elem in enumerate(l1):
        if len(l2) <= idx:
            break
        result.append((elem, l2[idx]))

    return result

        

