# Consigna:
 Se pide crear una versión CLI (Command Line Interface) del famoso juego  **piedra papel o tijeras**.
 
 Para esta versión implementaremos el modo de juego `Single Player` donde nuestro oponente será la computadora.
 
## Instrucciones del juego:
El juego se divide en rondas. Cada ronda, los participantes deben elegir en secreto (sin mostrar su elección al contrincante) alguna de los siguientes items: 
- Piedra
- Papel
- Tijera

Luego, todos los participantes muestran su elección (sin posibilidad de cambiar dicha elección). El ganador de dicha ronda será aquel que cumpla con alguna de las siguientes condiciones:
- Papel gana a Piedra.
- Tijera gana a Papel.
- Piedra gana a Tijera.
- **En caso de elegir el mismo item, se considera un empate y no hay ganador.**
En caso de haber un ganador de la ronda, se le asigna 1 punto a ese jugador.
El juego continua en rondas hasta que alguno de los participantes consiga sumar 3 puntos.

## Requerimientos:
- EL usuario debe ingresar un nombre
- En cada ronda el debemos mostrar la opción elegida por cada participante y quien es el ganador.
- En caso que alguno de los participantes logre alcanzar los 3 puntos, indicar quien ganó y finalizar el juego.

## Observaciones:
- Toda lógica del juego debe estar encapsulada en funciones.
- El scope global se reserva únicamente para la definición de constantes, import de bibliotecas y llamado a la función principal.
- Se permite el uso de la biblioteca `random` proveniente de la standard library de Python.
