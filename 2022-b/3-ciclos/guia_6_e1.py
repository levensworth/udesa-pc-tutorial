
PASSWORD = 'password'
MAX_INTENTS = 3


intent = 0
while intent < MAX_INTENTS:
    user_input = input('ingrese password: ')
    if user_input == PASSWORD:
        print('clave correcta!')
        break
    else:
        print(f'clave incorrecta! [intentos {intent + 1}/{MAX_INTENTS}]')
        intent += 1


