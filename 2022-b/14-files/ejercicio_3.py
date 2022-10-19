

from typing import Optional, List


AGENDA_PATH = 'agenda.csv'

CONTACT_HEADER = ['nombre', 'email']

def add_row(path: str, contact: list[str]) -> str:
    
    with open(path, 'a') as f:
        contact_row = ','.join(contact) + '\n'
        f.write(contact_row)

    return contact_row


def filter_rows(path: str, name: Optional[str] = None, email: Optional[str] = None) -> Optional[List[str]]:
    name_index = CONTACT_HEADER.index('nombre')
    email_index = CONTACT_HEADER.index('email')

    with open(path, 'r') as f:
        for contact_row in f:
            contact = contact_row.split(',')
            name_filter = name is None or contact[name_index].rstrip() == name
            email_filter =  email is None or contact[email_index].rstrip() == email

            if name_filter or email_filter:
                # this is a match
                return contact.split(',')

    return None

from typing import Callable, Dict

def add_contact(agenda: str):
    user_input = input('ingrese un nuevo nombre de contacto y su email separado por coma: ')
    name = user_input.split(',')[0]
    email = user_input.split(',')[1]
    add_row(agenda, [name, email])


def show_contact(agenda: str):
    user_input = input('nombre del contacto o el email? ')
    contact = filter_rows(agenda,name=user_input, email=user_input)
    if contact is None:
        print('no existe dicho usuario')
        return
    
    print(f'Nombre: {contact[0]} email: {contact[1]}')
    

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
    agenda = AGENDA_PATH


    while True:
        fn = show_menu_and_select(commands)
        fn(agenda)
    
if __name__ == '__main__':
    main()

                    



