

from typing import Any, Dict


def play_game() -> None:
    print('playing game')


def update_state(current_state: Dict) -> Dict:
    print('here we change things')
    
    possible_actions = {
        'mod status': lambda : print('modifting status'),
        'remove status': lambda : print('removing status'),
        'go back': lambda : print('saving updates')
    }
    show_commands('update status menu', possible_actions)
    return current_state

def quit():
    print('good bye m8')


def show_commands(title: str, commands: Dict) -> Any:

    print(title.upper())
    idxs = {}
    for idx, op in enumerate(commands):
        print(f'{op} -> press [{idx}]')
        idxs[str(idx)] = commands[op]
    
    while True:
        user_op =  input('select an option > ')
        if user_op in idxs:
            return idxs[user_op]()


def main():
    state = {
        'user_name': 'santi'
    }
    
    commands = {
        'play': play_game,
        'quit': quit,
        'update_satus': lambda : update_state(state)
    }

    show_commands('main menu', commands=commands)    

main()