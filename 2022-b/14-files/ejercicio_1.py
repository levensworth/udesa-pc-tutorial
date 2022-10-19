'''
Implemente un programa que permita guardar contactos en una agenda. El programa debe solicitar al usuario el ingreso
de los siguientes datos: Nombre, Apellido, Teléfono, Email y un campo de Observaciones. Para ello debe definir las
funciones ingresar_contacto() y guardar_contacto(), que serán utilizadas por el programa principal. La información
solicitada debe guardarse en un archivo con formato CSV (ejemplo: agenda.csv)

'''



from typing import Tuple
import os

AGENDA_PATH = 'agenda.csv'

CONTACT_COLUMNS = ['nombre', 'apellido', 'telefono', 'email', 'observacion']

def ingresar_contacto() -> Tuple[str]:
    name = input('ingrese nombre: ')
    surname = input('ingrese apellido: ')
    tel = input('ingrese telefono: ')
    email = input('ingrese el email: ')
    obs = input('ingrese alguna observacion: ')

    return (name, surname, tel, email, obs)

def guardar_contacto(path: str, contact: Tuple[str]) -> None:

    with open(path, 'a') as f:
        contact_row = ','.join(contact) + '\n'
        f.write(contact_row)



def prepare_file(path: str) -> None:
    '''
    Esta fuciœn chequea si el archivo no existe, en cuyo caso lo crea y agrega los headers.
    Caso contrario no hace nada.
    '''
    
    if os.path.exists(path):
        return 
    
    # agregamos el nombre de las columnas al archivo.

    with open(path, 'w') as f:
        f.write(CONTACT_COLUMNS)
    

def main():
    
    print('welcome to agenda!')
    print('to terminate de program press Ctrl + c at any given moment')
    
    prepare_file(AGENDA_PATH)
    
    while True:
        contacto = ingresar_contacto()
        guardar_contacto(AGENDA_PATH, contacto)
        
    
if __name__ == '__main__':
    main()
