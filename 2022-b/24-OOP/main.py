import os

import getch

from creatures import Walker
from game_engine import GameEngine
from map import Map

'''
Este jeugo tiene las siguientes funcionalidades aplicadas:

- Walker (personaje principal comandado por el usuario)
- Goblin (personajes secundarios que el se transforman en pierda al chocar paredes)
- Objetivo (salida del laberinto)

Se espera que:
puedan continuar la logica para que el usuario pueda tomar el pico al moverse sobre este.
Una vez el usuario tome el pico, este debe permitirle romper paredes.

No se contempla que el usuario interactue con los Goblins, pero puede pensar nuevos 
personajes que tengan funciones distintas a las del goblin.

'''

def main():
    map = Map(10, 10)
    walker = Walker('W', 30)
    engine = GameEngine(board=map, player=walker)
    os.system("clear")
    engine.show_state()
    user_input = getch.getch()
    while user_input != "q":
        os.system("clear")

        engine.compute_state(user_input)

        if engine.player_won():
            print("YOU WON!")
            exit()

        if engine.player_dead():
            print("YOU LOST!")
            exit()
        user_input = getch.getch()
    exit()


if __name__ == "__main__":
    main()
