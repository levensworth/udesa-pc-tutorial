
def get_balance(exp: str) -> int:
    
    if len(exp) == 0:
        return 0

    n = 0
    if exp[0] == '(':
        n = 1
    
    if exp[0] == ')':
        n = -1
    
    return n + get_balance(exp[1:])


    

