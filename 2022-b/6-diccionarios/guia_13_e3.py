from typing import Callable, Dict

def add_contact(agenda: Dict[str, str]):
    user_input = input('ingrese un nuevo nombre de contacto y su email separado por coma: ')
    name = user_input.split(',')[0]
    email = user_input.split(',')[1]
    agenda[name] = email


def show_contact(agenda: Dict[str, str]):
    user_input = input('nombre del contact? ')
    if user_input not in agenda:
        print('no existe dicho usuario')
    
    print(f'Nombre: {user_input} email: {agenda[user_input]}')
    


def quit(agenda: Dict[str, str]):
    print('good bye!') 
    exit()


def show_menu_and_select(menu: Dict[str, Callable]) -> Callable:
    options = {}
    for idx, name in enumerate(menu.keys(), 1):
        print(f'[{idx}] {name}')
        options[idx] = menu[name]

    option = int(input('que desea hacer? '))
    
    return options[option]

def main():

    commands = {
        'add contact': add_contact,
        'show contact': show_contact,
        'quit': quit
    }
    agenda = {}

    while True:
        fn = show_menu_and_select(commands)
        fn(agenda)
    

main()

                    


