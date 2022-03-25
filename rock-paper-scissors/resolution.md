# Pasos para la resolución:

## 1: Definir las acciones que supone la realizacion del enunciado.

En este paso, lo que definimos son los procedimientos genéricos que vamos a usar
para resolver nuestro problema.

0. Ingrese el nombre del usuario.
1. Obtener la opción del usuario (definidas por el juego).
2. Obtener la opción del jugador computadora.
3. Computar quien gano la partida y anunciarlo (mostrar en pantalla).
4. Si nadie ganó el juego, repetir step 1.
5. si un jugador ganó, mostrar su nombre en pantalla.



## 2: Fragmentar el problema en pequeños problemas:
La clave de todo problema se trata de entender el problema general como una suma
de pequeños problemas. Infromática no es la excepción, sino uno de los mayores exponentes de dicha regla.

Lo primero que debemos hacer es obsrevar nuestras acciones definidas en el primer punto.
Notaremos que hay acciones sencillas que podemos generar funciones para realizarlas como:

0. Obtener el nombre del usuario =>  puede ser definida con `def get_user_name() -> str:`
1. Obtener la opción del usuario => `def get_user_choice() -> str:`
2. Obtener la opción de la computadora => `def get_computer_choice() -> str:`
3. Computar quien es el ganador de una ronda => `def compute_round_winner(user1_option:str, user2_option: str) -> str:`
4. Determinar si alguno de los jugadores ganó el juego => `def is_winner(user_score: int) -> bool:`

Estas acciones son bien concretas y nos permiten comenzar a pensar el problema y desglozarlo en sus partes.

## 3: Entender la mecánica del problema:
En muchas ocaciones veremos que hay arquetipos (patrones) de comportamiento que se repiten en multiples situaciones. Esto es algo bueno, es un comienzo que nos permite encontrar una solución al problema rápidamente.
En este caso, debemos observar al ciclo principal. Dicho ciclo es el que comprende los pasos 1 a 4 en nuestra lista de acciones. Esto es el ciclo principal de nuestro programa, si analizamos juegos de mesa veremos que muchos mantienen un patrón similar. Esto significa que tienen un tipo de lógica similar a:
1. Tomar las acciones o movientos de cada usuario.
2. Computar el nuevo estado del juego.
3. En caso que no haya ganadores, volver al punto 1.

Estos pasos son lo que representa el corazón de nuestro programa y es lo que vamos a incluir dentro de la función principal del mismo.

```
def game():
    # inicializar lso estados del juego.
    ...
    # main loop
    while not <winning_condition>:
        ....
    
    # toma de acciones en caso de un ganador.
```

## 4: Iterar sobre la solución:
Una vez que tenemos ciertos elementos del juego y entendemos la mecánica principal del mismo.
Nos toca comenzar a iterar sobre los pasos que faltan para poder tener una versión funcional del program, esto significa una versión que cumpla con todos los requerimientos. 
Una vez que tenemos esto, se trata de revisar nuestro código y comenzar a ver patrones comunes en 
las funciones o procedimientos que escribimos para así lograr una versión más clara y fácil de extender.

### Obs!
* una buena 'Rule of thumb' para saber si nuestra solución es correcta, es que la función principal,
consista en llamado a funciones y casi no contenga lóigca excepto el loop principal.
* Las funciones deben tener sentido, es decir que el comportamiento que encapsulamos dentro tiene que ser coherente con lo que esperamos de la función.
* Recuerde que la solución propuesta en este caso, no es única ni la mejor. Simplemente es una de las posibles y sirve de guía.