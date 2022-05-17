
# Ejercicios:

1. Implementar una función recursiva que reciba una lista de enteros y retorne la suma de sus elementos.
2. Implementar la función de Fibonacci de manera recurrente.
3. Implementar una función `rec_loop_print(txt, n)` que muestre `n` veces el string `txt`.  
4. Implementar una función recursiva `get_balance` que dado una expresión matemática (en string)
    retorne el balance de parentesis.
    Ejemplo: `56 + (a - 7 - ( 12 + c) - t * 678)` retornaría 0, significando que está balanceada.
    `56 + (a - 7 -  12 + c) - t * 678)` retornaría distinto de cero, didicando que no está balanceada.
    
5. Implementar la funcion `generate_possible_sequences` tal que  
    dada una lista de N caracteres, retorne los posibles strings 
    de logitud `k`.
    **Hint:** La solución, solo requiere dos parámetros `expression` y `k`. Considerar como caso base 
    `k = 1`, re resultado esperado sería una lista donde cada elemento de `expression` sea un elemento
    del resultado.

```
    >>> generate_possible_sequences(['a', 'b', 'c'], 1)
    >>> ['a', 'b', 'c']
    >>> generate_possible_sequences(['a', 'b', 'c'], 2)
    >>> ['aa', 'ba', 'ca', 'ab', 'bb', 'cb', 'ac', 'bc', 'cc']
    
```

6. un mapa se puede entender como una matriz de NxM la cual se representa como una lista de listas en el lenguaje. Dado un mapa, donde los valores de cada celda serán 0 si no hay nada y 1 si hay pared, implementar una función `are_connected(map, from_point, to_point)` que reciba un mapa y 2 coordenadas y retorne si existe un camino libre que conecte los dos.


