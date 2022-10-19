

def rec_sqrt(number: int, accuracy: int) -> float:
    
    if accuracy == 0:
        return number

    prev = rec_sqrt(number, accuracy-1)

    return 0.5 * ((number / prev) + prev)
    


