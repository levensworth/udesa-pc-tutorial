# Consignas
Para estas consignas, recordar que un string es una lista de caracteres. 
Es importante pensar en módularizar el comportamiento, descoponer cada enuncia en acciones más pequeñas y atómicas que podamos resolver facilmente.

### Atención:
Antes de resolver lso ejercicios a continuación, primero es aconsejable leer `summary.md` para refrescar el conocimiento sobre el manejo de listas. Luego comenzar por `warmup.md`, el cual es un set de ejercicios más sencillos con el objetivo de ampliar su panorama sobre listas.

1. dado un patrón de string, devolver la representación del patrón. 
Ejemplo: 'a4h ok3' representa el string: "aaaah okkk" 
el uso de la función sería:
```
>>>decode_str('a4h ok3') 
>>> "aaaah okkk" 
```

2.  Escribir una función que reciba un patrón y un string y retorne si el string cumple con el patrón. 
El patrón debe estar compuesto por:
letras, numeros, espacios, '?', o '*'.
-> '?' es un comodín y puede representar cualquier caracter.
-> '*' es un comodín multiple y representa que cualquier secuencia de caracteres es correcta.


ejemplo:
```
is_match('ho?a', 'hola') devuelve True
is_match('ho?a', 'hoja') devuelve True
is_match('ho?a', 'toca') devuelve False
is_match('ho?a', 'hol') devuelve False
is_match('ho*', 'hola como estas todo esto es valido') devuelve True

```
