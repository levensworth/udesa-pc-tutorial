
def print_rec_loop(txt: str, n: int) -> None:
    '''
    Muestra en pantalla N veces el valor de txt.
    '''

    if n <= 0: 
        return
    
    print(txt)
    print_rec_loop(txt, n-1)

def print_rec_loop_2(txt: str, n: int) -> None:
    '''
    Muestra en pantall N veces el valor de txt seguido
    del inidce por el que se encuentra.
    '''

    if n <= 0:
        return 
    
    print_rec_loop_2(txt, n-1)
    print(txt, n)
