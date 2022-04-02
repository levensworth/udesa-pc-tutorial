# Ejercicios para entrenar:
Esta es una serie de ejercicios para practicar el uso de listas y su contexto en 
la programación.


1. Escriba una función llamada `filter_even`  que reciba una lista de enteros y retorne una nueva
   lista que contenga los elementos pares del arreglo original.

2. Escriba una función llamada `filter_multiples_of_n` que reciba una lista de enteros y un entero positivo, retorne una nueva lista que contenga los elementos multiples de n del arreglo original.

3. Escriba una función llamada `has_negative` quw reciba una lista de enteros y retorne True si la lista contiene negativos, caso contrario False.

4. Escriba una función llamada `abs_dif` que reciba una lista de numeros reales y devuelva la mayor diferencia entre elementos consecutivos. Tener en cuenta que pueden haber negativos. En caso de tener una lista de 1 elemento, retornar 0.

5. Escriba una función `find_elem` que reciba una lista y un elemnto, retorne True si el elemnto se encuentra almenos 1 vez en la lista caso contrario False.

6. Escriba una función `remove_duplicates` que reciba una lista de enteros **desordenados** y retorne una nueva lista sin elementos repetidos. 
   a. Utilizar `find_elem`
   b. Utilizar `in` 

7. Reimplementar la función anterior, para listas ordenadas.

8. Escribir una función `sort_list` que reciba una lista de enteros  desordenados y retorne una nueva lista con los elementos ordenados. Este ejercicio no puede utilizar funciones de la biblitoeca estándar de Python.

9. Implementar una función `merge_list` que reciba 2 listas de enteros postivios ordenados y sin repetidos. Retorne una nueva lista ordenada que contenga la unión de los dos arreglos, no debe contener repetidos.
```
merge_list([1,2,3], [2,3,4])
[1,2,3,4]
merge_list([1,4,6,11], [2])
[1,2,4,6,11]
```

9.  Reimplementar la función anterior considerando que las listas inciales pueden tener repetidos pero la función debe devolver la unión sin repetidos.

10. Escribir una función `filter_list` que reciba una lista y un predicado[1]. Retorne una nueva lista que contenga los elementos que cumplan con el predicado. 
   [1] un predicado es una función que reciba un elemnto y retorne un `bool`. Ejemplos de predicados son:
   -  Función `is_even` que reciba un número y retorne True si es multiplode 2
   -  Función `is_prime` que reciba un número y retornce True si es primo.
  
  ```
  El uso de este encunciado sería
  
   def is_even(num: int) -> bool:
      return num % 2 == 0

   lista = [1,2,3,4,5]

   filter_list(lista, is_even) # retorna una nueva lista: [2,4]

  ```
  