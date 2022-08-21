'''
Enunciado:
Escribir programas que resuelvan los siguientes problemas:

Dado un año indicar si es bisiesto.

¿Cómo sé si un año es bisiesto?

Un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

Dado un mes y un año, imprimir la cantidad de días correspondientes (por ejemplo: 2022 y 11 devuelve 30).

Dada una fecha (día, mes, año), indicar si es válida o no.
Dada una fecha, indicar los días que faltan hasta fin de mes.
Dada una fecha, indicar los días que faltan hasta fin de año.
Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días.
'''
# constants

DAYS_IN_YEAR = 365
DAYS_IN_LEAP_YEAR = DAYS_IN_YEAR + 1

#a.  ver si un año es biciesto:

year = int(input('un año: ')) # poner el año que desea verificar
div_by_4 = year % 4 == 0
div_by_100 = year % 100 == 0
div_by_400 = year % 400 == 0

is_leap_year = False
if div_by_4 and not div_by_100:
    is_leap_year = True
elif div_by_4 and div_by_100 and div_by_400:
    is_leap_year = True
else:
    pass # no hago nada porque is_leap_year ya es false


message = '' if is_leap_year else 'no'
print(f'{year} {message} es un año biciesto!')   

# b. dado un mes y un año indicar la cantidad de dias que tiene dicho mes

# para facilitar el enunciado, voy a tomar el año del punto a.
# de esta manera ya tenemos el valor de si es biciesto o no.

month = int(input('ingrese el numero de mes: '))


if month == 2:
    amount_of_days = 29 if is_leap_year else 28
elif str(month) in '1 3 5 7 8 10 12':
    # estoy utilizando el truco del operador 'in' para strings
    # es importante saber jugar con los tipos de datos y sus propiedades.
    # para que esto funcione, es importante que primero chequee el mes 2
    # dado que sino, el string '2' dara true al encontrarse dentro de '1 3 5 7 8 10 12'
    # entonces es un mes de 31
    amount_of_days = 31
else:
    amount_of_days = 30

print(f'la cantidad de dias en este mes es: {amount_of_days}')


# c.Dada una fecha, indicar los días que faltan hasta fin de mes.
# nuevamente voy a utilizar el año y mes ya ingresados para no volver a pedirlos

day = int(input('ingrese un dia: '))

if day > 0 and day < amount_of_days:
    print("es una fecha válida")
    print(f'faltan {amount_of_days - day} hasta fin de mes!')
else:
    print('es una fecha inválida')


# e. Dada una fecha, indicar los días que faltan hasta fin de año.
days_left_in_month = amount_of_days - day
if month == 12:
    days_left = days_left_in_month

elif month == 11:
    days_left = days_left_in_month + 31

elif month == 10:
    days_left = days_left_in_month + 31 + 30

elif month == 9:
    days_left = days_left_in_month + 31*2 + 30
    
elif month == 8:
    days_left = days_left_in_month + 31 * 2 + 30 * 2

elif month == 7:
    days_left = days_left_in_month + 31 * 3 + 30 * 2

elif month == 6:
    days_left = days_left_in_month + 31 * 3 + 30 * 3

elif month == 5:
    days_left = days_left_in_month + 31 * 4 + 30 * 3

elif month == 4:
    days_left = days_left_in_month + 31 * 4 + 30 * 4

elif month == 3:
    days_left = days_left_in_month + 31 * 5 + 30 * 4

elif month == 2:
    days_left = days_left_in_month + 31 * 5 + 30 * 5

elif month == 1:
    if is_leap_year:
        days_feb = 29
    else:
        days_feb = 28

    days_left = days_left_in_month + 31 * 5 + 30 * 5 + days_feb

print(f'Faltan {days_left} para fin de año')

# f. indicar los dias transcurridos desde principio de año
# nuevamente utilizando los resultados de puntos previos
days_of_year = DAYS_IN_LEAP_YEAR if is_leap_year else DAYS_IN_YEAR

days_from_begining_of_year = days_of_year - days_left
print(f'pasaron {days_from_begining_of_year} desde el principio de año')

#g. dadas 2 fechas (dias, mes, año) indicar la cantidad de años meses y dias transcurridos
# tomo como que la primera fecha lo que ya tomamos en puntos anteriores

'''
En el siguiente fragmento itnentaremos tomar la diferencia entre 2 fechas, asumimos un par de cosas:
1. la fecha ingresada con anterioridad será la que ya utilizamos en los puntos previos
2. la nueva fecha que nos daran será posterior a la que nos dieron antes
3. cuando la cantidad de días entre 2 fechas sea mayor a 30 consideraremos que hay 1 mes de tiempo.

procedimiento "logico del codigo"

en la siguiente solución lo que se intenta proyectar es el siguiente approach:
1. tomo la dif de dias entre la fecha inicial y la final (este num puede ser mayor a 30)
2. tomo la dif entre el mes ingresado  como final y el siguiente mes al que ingresor incial
    esto es porque tomé la diferencia de dias contando los dias faltantes hasta fin de mes.
3. chequeo si la diferencia de dias es mayor a 30 dias, en cuyo caso sumo 1 mes a la dif de meses
4. tomo la dif de años contabilizando los años que se ingresaron.
5. dado que si la dif de mese es menor que 12 podemos estar contabilizando un año extra, verficamos esto.
'''

year_from = year
month_from = month
day_from = day

print('debe ingresa una fecha posterior a la que ingresó previamente')
day_to = int(input('ingrese un día: '))
month_to = int(input('ingrese un mes: '))
year_to = int(input('ingrese un año: '))


dif_days = days_left_in_month + day_to

delta_day = dif_days % 30
# tomo la dif de meses con respecto al mes siguiente porque
# estoy considerandoa el mes actual en la dif de dias 

dif_month = month_to - (month_from + 1)
# en este punto sumo, que si la cantidad de dias es mayor al equivalente de 1 mes
# efectivamente sumamos 1 mes a la diferencia total entre fechas
# el valor de 30 es arbitrario dado que usualmente en este tipo de cálculos
# asumimos quea por cada 30 dias sumamos 1 mes a la dif de meses.
dif_month += dif_days // 30

delta_month = dif_month % 12 

delta_year = year_to - year_from 

if delta_year > 0:
    # si la dif de meses es menor a 12 hay que restar un año
    delta_year -= 1 if dif_month > 0 else 0 


print(f'pasarons {delta_year:02d} años {delta_month:02d} meses y {delta_day:02d} dias')




