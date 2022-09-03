
#  ejercicio 1 

# A.

n = int(input('Ingrese un año: '))
modulo = abs(n)
if n > 0:
    siglo = (n - 1) / 100
    cuenta = siglo + 1
    print(f'Siglo {cuenta} e. c.')

elif n < 0:
    siglo = (modulo - 1) // 100
    cuenta  = siglo +1
    print(f'Siglo {cuenta} a. e. c.')
else:
    print('no existe  el siglo para el año 0.')




# B.

planet = input('ingrese el nombre de un planeta: ')
planet = planet

if planet == 'mercurio':
    print('no tiene')
elif planet == 'venus':
    print('no tiene')
elif planet == 'tierra':
    print('si tiene')
elif planet == 'marte':
    print('si tiene')
elif planet == 'jupyter':
    print('si tiene')
elif planet == 'saturno':
    print('si tiene')
elif planet == 'urano':
    print('si tiene')  
else:
    print('lo ingresado no es valido')


#C.
number = int(input('ingrese un numero'))

if number > 0:
    sign = 'positivo'

    print(f'el numero es {sign}')


    sqrt_number = number ** 0.5

    if sqrt_number == int(sqrt_number):
        print('y es un cuadrado perfecto')

    if number % 2 == 0:
        is_even = True
    else:
        is_even = False

    print(f'y es {"par" if is_even else "impar"}')

