'''
Enunciado:
Escriba un programa que imprima N números de la secuencia de Fibonacci, 
donde N es un parámetro de la función.
'''

n = 10 # el valor es simplemente de ejemplo

prev = 1
current = 1
print(current)
while n > 0:
    print(current)
    aux = current
    current = current + prev
    prev = aux
    n -= 1


    
    
    

