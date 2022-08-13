# Recursión:
Recursion es un concepto de programación que tiene sus bases en matemática, se utiliza en ramas como
matemática discreta, teorīa de grafos, probabilidad y algebra entre otras.
Es un conepto importante dado que, cuando el problema presenta un carácter recursivo, la soluciones
son frecuentemente más sencillas de entender y de implementar. 

Este método potente de diseño y resolución de problemas, tiene una relación natural con la inducción
y por ello facilita la resolución de problemas y diseño de algoritmos.

## Como encarar los problemas:
Generalmente los problemas de recursión tiene 3 estructuras básicas. Lo más importante es encontrar 
la parte recursiva del problema, por ejemplo:
- Si el problema trata sobre listas, recordar que una lista tiene un definición recursiva
  del tipo: "una lista es un elemento seguido de una sublista"
- Si el problema nos dá un string, también podemos entenderlo como un caracter seguido de un substring.
- Si el enunciado trata sobre números, escribir el pseudo algoritmo que nos piden para encontrar la parte recursiva (ejemplo: Fibonacci).
Dentro de las estructuras básicas encontramos:

1. Recursión sobre la definición del problema. Estos son los casos como fibonacci, donde la recursión está
   explicita en la definición del problema en si.

2. Recursión sobre la estructura de los parámetros. Estos son los casos donde nos pasan un tipo de argumento que tiene una definición recursiva y sobre la que tenemos que moldear la solución como el caso de sumar los elementos de una lista.

3. Recursión para backtracking. Estos problemas son normalmente los que requieren que encontremos todas las posibilidades de una secuencia o satisfacer los constrains de un problema. 


Luego de encontrar la estructura, en conveniente definir el/los casos base del problema. Generalemnte 
este paso determina el tipo de solución que tendremos. Recordar que en una solución recursiva, siempre 
tenemos un camino de "ida" hacia el caso base y un camino de "vuelta" desde el caso base. Muchas veces 
depende el problema debemos hacer cosas en el camino de "ida" y otras en el camino de "vuelta" pero esto 
viene determinado por como pensemos el caso base. 

**obs** Lo que hagamos `antes` del llamado recursivo ocurre en nuestro camino "hacia" el caso base y 
lo que hagamos `luego` del llamado recursivo ocurre en el camino "de retorno" desde el caso base. 


## Práctica:
Realizar los ejercicios de `statement.md`, luego chequear las soluciones con la carpeta `/solutions`.
