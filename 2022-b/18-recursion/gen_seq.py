"""
Implementar la funcion `generate_possible_sequences` tal que  
dada una lista de N caracteres, retorne los posibles strings 
de logitud `k`.
**Hint:** La solución, solo requiere dos parámetros `expression` y `k`. Considerar como caso base 
`k = 1`, le resultado esperado sería una lista donde cada elemento de `expression` sea un elemento
del resultado.


>>> generate_possible_sequences(['a', 'b', 'c'], 1)
>>> ['a', 'b', 'c']
>>> generate_possible_sequences(['a', 'b', 'c'], 2)
>>> ['aa', 'ba', 'ca', 'ab', 'bb', 'cb', 'ac', 'bc', 'cc']
"""












from typing import List


def generate_possible_sequences(seq: List[str], k: int) -> List[str]:
    
    if k == 0:
        return []

    if k == 1:
        return list(seq) # genero una nueva sequencia para no devolver la misma instancia

    prev_sequences = generate_possible_sequences(seq, k-1)

    sequences = []
    for string in seq:
        for prev_seq in prev_sequences:
            sequences.append(prev_seq + string)
    
    return sequences


print(generate_possible_sequences(['a', 'b', 'c'], 3))