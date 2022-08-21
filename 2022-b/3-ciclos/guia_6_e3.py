import time
# definimos las constantes para no utilizar magic number
SEC_PER_HOUR = 3600
SEC_PER_MIN  = 60
MIN_PER_HOUR = 60


hours = int(input('Ingrese la cantidad de horas: '))
minutes = int(input('Ingrese la cantidad de minutos: '))
sec = int(input('Ingrese la cantidad de segundos: '))

amount_of_secs = hours * SEC_PER_HOUR + minutes * SEC_PER_MIN + sec


while amount_of_secs > 0:
    hours_left =  amount_of_secs // SEC_PER_HOUR
    minutes_left = (amount_of_secs // SEC_PER_MIN) % MIN_PER_HOUR
    seconds_left = amount_of_secs % SEC_PER_MIN
    # indicamos el /r como caracter final para sobre escribir la linea
    print(f'{hours:02d}:{minutes_left:02d}:{seconds_left:02d}', end='\r')

    time.sleep(1)
    amount_of_secs -= 1