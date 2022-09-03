import random

'''
Ejercicio maso de cartas francesas.
Clase tutorial 9
'''



def main():
    print('bienvenido al juego')
    user_value = input('presione ENTER para seguir o \'q\' para salir')
    
    if user_value == 'q':
        print('bye!')
        exit()

    throw_card()

def throw_card():
    """Genera una carta al azar y la imprime en pantalla"""
    # tomar una carta al azar
    valor = random.randint(1, 13)
    palo = random.randint(1, 4)

    # generar la carta (su string representation)
    valor_str = get_value_str(valor)
    palo_str = get_symbol_str(palo)
    card_repr = gen_card(valor_str, palo_str)

    # print en pantalla de dicha carta
    print(card_repr)


def gen_card(n: str, s: str):
    """ Retorna un string con el ascii de la carta (de valor n y figura s) """
    template = f'''+{'-'*11}+\n'''
    template += f'''|{s}{n}{' '*8} |\n'''
    for _ in range(9):
        template += f"|{' '*11}|\n"
    
    template += f'''| {' '*8}{n}{s}|\n'''
    template += f'''+{'-'*11}+\n'''

    return template


def get_symbol_str(symbol_number: int) -> str:
    """ Mapea un número int (entre 1 y 4) al caracter del símbolo de la carta """
    symbol = None
    if symbol_number == 1:
        symbol = chr(9824)
    
    if symbol_number == 2:
        symbol = chr(9830)
    
    if symbol_number == 3:
        symbol = chr(9829)

    if symbol_number == 4:
        symbol = chr(9827)

    return symbol

def get_value_str(value_number: int) -> str:
    """ Mapea un número int (entre 1 y 13) al caracter del valor de la carta """
    result = None
    if value_number > 1 and  value_number < 11:
        result =  str(value_number)

    if value_number == 1:
        result =  'A'
    
    if value_number == 11:
        result =  'J'
    
    if value_number == 12:
        result =  'Q'
    
    if value_number == 13:
        result =  'K'

    return result
     
    

if __name__ == '__main__':
    main()



