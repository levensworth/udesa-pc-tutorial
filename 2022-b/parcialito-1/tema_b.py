
#  ejercicio 1 

# A.

n = int(input('Ingrese un año: '))
modulo = abs(n)
if n > 0:
    siglo = (n - 1) / 1000
    cuenta = siglo + 1
    print(f'Milenio {cuenta} e. c.')

elif n < 0:
    siglo = (modulo - 1) // 1000
    cuenta  = siglo +1
    print(f'Milenio {cuenta} a. e. c.')
else:
    print('no existe  el siglo para el año 0.')


# B.

planet = int(input('Ingrese el numero de un planeta: '))
planet_name = ''
if planet == 1:
    planet_name = 'Mercurio'
elif planet == 2:
    planet_name = 'Venus'
elif planet == 3:
    planet_name = 'Marte'
elif planet == 4:
    planet_name = 'Tierra'
elif planet == 5:
    planet_name = 'Jupiter'
elif planet == 6:
    planet_name = 'Saturno'
elif planet == 7:
    planet_name = 'Urano'
elif planet == 8:
    planet_name = 'Neptuno'


# C
planet = input('Plantea? ')

if planet == 'Mercurio' or planet == 'Venus' \
    or planet == 'Tierra' or planet == 'Marte':
    print(f'{planet} es rocoso e interior')

elif planet == 'Jupiter' or planet == 'Saturno':
    print(f'{planet} es exterior')
    print(f'y gigante gaseoso')
elif planet == 'Urano' or planet == 'Neptuno':
    print(f'{planet} es exterior')
    print(f'y gigange helado')
