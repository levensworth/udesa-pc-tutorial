# Manejos de Listas
Este documento intenta ser una pequeña guía en el uso de listas.

## Definición: Lista
Una lista es una estructura dentro del lenguaje Python definida como 
representación de una secuencia de elementos.
La misma tiene ciertas propiedades importantes:
- Las listas tienen un número de elementos dentro de ellas.
- Pueden poseer elementos de diferente naturaleza, es decir `int`, `float`, otras listas, etc.
- Son `mutables` es decir que podemos reemplazar un elemento en una posición dada por otro.
- Son extensibles, significa que podemos sumar más elementos. Por defecto, solo podemos insertar al final del arreglo.
  
## Creación:
Para crear una lista se puede hacer de varias formas:
- Inicializar una lista vacía: `[]`
- Inicializar una lista con elementos: `[1, 2, 3, 'hola']`
- Utilizando la función build-in: `list()`


## Operadores:
Como vimos con otros tipos de datos dentro de Python, las listas tienen un comportamiento frente a cada operador que corresponde a 
su mappeo dentro del universo de listas.
1. `bool(lista)` : Las listas pueden ser casteadas a bool. El lenguaje asume que una lista vacía tiene el valor de `False` y una lista con elementos `True`.
2. `len(lista)`: Existe una función build-in dentro de Python que nos permite saber la cantidad de elementos de una lista. `len(lista)` devuelve el número de elementos.
3. `lista == lista`: La comparación entre listas se realiza `element-wise` significa solo se toman 2 listas iguales si sus elmentos son iguales y se encuentran en la misma posición. 
4. `lista[idx]`: Podemos obtener el elemento en una posición dada utilizando la notación `[posición]`. Recordar que las listas son 0-index based.
   Es interesante notar que podemos pasar valores negativos como indices, Python interpreta los mismos recorriendo la lista desde el final en sentido opuesto. 
   Ejemplo: lista[-1] Nos retorna el último elemento, lista[-2] el ante úiltimo y así sucesivamente.
5. `for elem in lista`: las listas son `iterables` signifca que podemos recorrer todos sus elementos utilizando un ciclo cerrado (`for`).
6. `elem in lista`: las utilizando la palabra reservada `in` podemos chequear si un elemnto existe dentro de la lista sin considerar posición.
7. `lista.pop() y lista.pop(idx)`: las listas permiten eleminar elemntos de ellas por indice, utilizando `pop()`, si no pasamos un indice la lista elimina el último elemento.
8. `lista.remove(elemento)`: Las listas también nos permiten eliminar elementos particulares, en este caso debemos pasar el elemnto que queremos eliminar. 

## Slicing:
Python tiene ciertas particularidades que hacen el uso de listas distinto a muchos lenguajes. Una de estas particularidades se muestra en el slicing de listas. La acción de slicing se refiere a tomar una sublista de la lista initial.
```
>>> lista = [1,2,3,4]
>>> lista[1:3]
    [2, 3]
>>> lista[1:-1]
    [2,3]
>>> lista[2:]
    [3, 4]
>>> lista[90:]
    []
```
Es slicing se trata de pasar un rango de inidices de la forma `n:n` al operador `[]` como se observa en el ejemplo anterior. Luego Python interpreta que deseamos obtener una nueva lista que solo contenga los elementos del arreglo original comprendidos en el intervalor cerrado por izquiera y abierto por derecha entre esos indices. 
En el caso que no escribamos alguno de los indices (el principio o el final) como `:n` o `n:`, el lenguaje asume que deseamos una sublista desde el comienzo del arreglo original o hasta el final del mismo respectivamente. En caso de no escribir niguno `[:]` retorna una compia exacta del arrelgo original.
Finalmente, en el caso que el rango comprendido por los indices no pertenezca al arreglo (pedir el intervalo entre `90:100`) el lenguaje simplemente 
retorna una nueva lista vacía.

## Listas y funciones:
Vimos que las funciones son uno de los pilares dentro de programación y nos permite encapsular una par de nuestra aplicación incrementando la capacidad de reusar cierto código. Algo a tener encuentra en el uso de funciones con listas es la mutabilidad de las mismas.
Cuando llamamos a una función `fun(lista)` y le pasamos nuestra lista de elementos como argumento. La función tiene ahora una referencia a la lista original, es decir que si la lista sufre modificaciones en el procesamiento dentro de la función, esos cambios afectan al comportamiento posterior dentro de nuestro programa. 
Ejemplo: 
```
>>> lista = [1,2,3,4]
>>> lista 
>>> [1,2,3,4]
>>> remover_pares(lista) # esta función suponemos que remueve los elementos pares de la lista
>>> lista
>>> [1,3]
```
Es muy importante tener en cuenta y aclarar cuando este comportamiento ocurre dentro de nuestras funciones, dado que la persona que utiliza nuestras funciones puede no estar al tanto de dicho comportamiento.


## Obs:
`None` y `[]` no son lo mismo, La lista vacía se escribe como `[]` mientras que la ausencia de lista es `None`. 
