# Testing 

En Programación, es muy importante que nuestra solución pueda dar confianza de que realmente resuelve lo pedido. Generalmente para hacer esto, lo que hacemos es "testear" nuestro código. Lo cual se reduce a poner a prueba nuestra solución bajo casos de prueba que podemos predecir su resultado esperado.

## Unit Tests:
El tipo de test que veremos y uno de los más utilizados, es el llamado test unitario o "unit test". Se refieren a que solo están enfocados en corroborar que una cierta parte de nuestro programa funcione según lo esperado. Estos test son llamados: test de caja negra o "black box testing" dado que cuando desarrollamos test unitarios, no se supone que sabemos como funciona por dentro este pedazo de código. Todo lo contrario, no nos interesa como genera sus resultados. El test unitario solo debe asegurar que dados los requerimientos iniciales, el resultado final es el esperado.

## Porque los tests:
Porque una solución que puede ser testeada tiene mucho más valor que aquella que no. Dado que los tests (si se hacen correctamente) nos dan ciertas ventajas:
- En caso que una porción del código no quede bien documentada, el test puede mostrar cual es su comportamiento esperado.
- En caso que se introduzcan cambios en la solución, tenemos una forma de poder verificar que dichos cambios no rompieron el "contrato" de esa solución.
- Nos obliga a pensar las soluciones de forma que puedan ser explicables y verificables por un test. Esto es difícil de entender sino es en un ejemplo práctico. Pero esecialmente, significa que nuestras soluciones tenderán a utilizar menos variables globales, estados ocultos y comenzarán a esperar parámetros que den el estado inicial de lo que realmente queremos hacer (ayudando al principio de responsabilidad única).
  
## Estrctura de un test:
Los test unitarios, sin importar el lenguaje y el framework que se utilice, llevan una estrctura básica que se desgloza en los siguientes aspectos:

- **given**: Son aquellos objetos, resultados, funciones, atributos, etc que nuestro código a testear requiere par comenzar. Ejemplo: en el caso que lo que vamos a testear sea una función que espera parámetros, dichos parámetros serían los    `givens`
- **when**: Es el resultado de ejecutar dicho código que deseamos testear. Ya sea llamar a la función, crear el objeto, etc.
- **then**: son las evaluaciones "Pruebas" que determinan si el resultado del **when** con los **givens** provistos es el esperado. Normalmente, estas evaluaciones se hacen utilizando `assert`s y escribiendo una condición lógica que pruebe el aspecto que nos interesa. Una condición puede ser que una lista sea de longitud `N`, que el elemento en la posición `i` sea el esperado, etc.


## Como seguir:
Realizar los ejercicios pedidos en `steatement.md` y luego realizar pruebas utilizando la biblioteca `pytest` la cual pueden descargar utilizando el comando `conda install pytest` desde su terminal.


