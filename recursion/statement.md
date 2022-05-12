
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



