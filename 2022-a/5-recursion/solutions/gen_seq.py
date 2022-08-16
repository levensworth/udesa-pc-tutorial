from typing import List

'''
Esto es un concepto un poco mas avanzado, llamado backtracking.
El concepto general para poder llegar a la solución es que debemos
pensar muy bien cual es el caso base dado que la implementación dependera
de eso. 

Comienzen por pensar que solo reciben k mayor a 0 y piensen como caso base
k = 1. De esta forma pueden, considerar que en el caso base, solo debemos devolver
la lista de todos los caracteres que nos pasaron.

Luego, para seguir el caso recursivo. Es importante pensar que suponemos que nos devuelve
el llamado recursivo anterior. 

'''


def generate_possible_sequences(txt: str, k: int) -> List[str]:
    # caso de emergencia
    if k == 0:
        return []
    # caso base
    if k == 1:
        return list(txt)

    possible_sub_seq = generate_possible_sequences(txt, k-1)
    new_seq = []
    for letter in txt:
        for seq in possible_sub_seq:
            new_seq.append(seq+letter)
    
    return new_seq

