import random
MAX_NUM = 200
MAX_TRIES = 20
magic_number = random.randint(0, MAX_NUM)

for i in range(MAX_TRIES):
    print(f'quedan {MAX_TRIES - i} intentos')
    user_guess = int(input(f'ingrese un numero entre 0 y {MAX_NUM}'))
    if user_guess > MAX_NUM:
        print('numero muy grande! perdes un turno')
        continue
    
    if user_guess == magic_number:
        print(f'ganaste! el numero es {magic_number} lo lograste en {i} intentos')
        exit()

    if user_guess < magic_number:
        print('el numero es mas grande')
    else:
        print('el numero es mas chico')

print(f'no lograste encontrar el numero {magic_number} en {MAX_TRIES}')

    
