

# Ejercicios:
Primero resuelva los siguiente enunciados.

1. Escribir una función `zip_lists(l1: List, l2: List)` que reciba 2 listas (`l1` y `l2`) y retorne una nueva lista que contenga tuplas con los elementos de cada lista que se encuentren 
en dicha posición. 
Ejemplo:
    ```
        >>> zip_lists([1,2,3], ['a', 'b', 'c'])
        >>> [(1, 'a'), (2, 'b'), (3, 'c')]
    ```

En caso que alguna de las listas sea más corta, la lista resultante solo debe contener hasta el último elemento de la lista más corta.
Ejemplo: 
    ```
        >>> zip_lists([1,2,3], ['a', 'b',])
        >>> [(1, 'a'), (2, 'b')]
    ```

2. Escribir una función `counter(txt)` que reciba un string y retorne una lista que contenga la frecuencia de cada palabra en el string. Contemplar que el string es una cadena de palabras separada por espacios. 
   el resultado debe tener el siguiente formato: `[('palabra', 20), ('segunda', 4)...]`
3. Escribir una función que dado una lista retore la lista invertida.
4. Escribir una funcion `fibonacci(n)` tal que reciba un indice y retorne el N-ésimo termino
   de la secuencia Fibonacci.
5. Resuelva el problema anterior utilizando diccionarios.
6. Escriba una función `time_it(f, args)` que reciba una función `f` y una lista `args` y retorne el tiempo que tarda el llamado a la función `f` con los argumentos `args`.


Utilice el módulo `pytest` para generar 1 test por cada función ya creada.

