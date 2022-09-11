'''
Dada la siguiente lista de colores
colores = ['azul', 'rojo', 'verde']
Imprima el siguiente mensaje de manera tal que para cada color muestre:
'El color actual es <color> y al anterior fue <color anterior>'

'''

colores = ['azul', 'verde', 'rojo']


# iterando sobre la lista:
cursor = [None, None]

for elem in colores:
    cursor[1] = cursor[0]
    cursor[0] = elem
    print(f"El color actual es {cursor[0]} y el anterior fue {cursor[1] if cursor[1] else 'ninguno'}")

    

#  haciendo indexing:
cursor = [None, None]

for idx in range(len(colores)):
    
    cursor[1] = cursor[0]
    cursor[0] = colores[idx]
    print(f"El color actual es {cursor[0]} y el anterior fue {cursor[1] if cursor[1] else 'ninguno'}")
