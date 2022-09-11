# Parte A
# Dado el siguiente código, implemente lo mismo pero usando lista de compresión
lista_1 = [1,2,3,4,5,6,7,8,9,10]
lista_2 = [x*2 + 1 for x in lista_1]
print(lista_2)


# Parte B
# Repita lo mismo pero para el siguiente código (note el agregado de una condición)

lista_1 = [1,2,3,4,5,6,7,8,9,10]
lista_2 = [x*2 + 1 for x in lista_1 if not x%2]


