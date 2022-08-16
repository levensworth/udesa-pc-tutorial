'''
Implemente un programa que genere una variable tipo string, de modo tal que al
imprimirla se vea la imagen de caracteres a continuación:
 ___________
|           |
|  *     *  |
|  *  *  *  |
|  *     *  |
|___________|
La misma debe tener 13 caracteres de ancho. Sólo pueden utilizarse los caracteres
' ' (espacio) , '|' (pleca) , '*' (asterisco) y '_' (guión bajo) . También puede
utilizarse el salto de línea '\n'.
'''

max_width = 13

horizontal_bound = '_' * max_width

empty_slot = '|' + ' ' * (max_width - 2) + '|'

two_pointers = '|  *' + ' ' * (max_width - 8) + '*  |'

middle = '|  *  *  *  |'

empty_slot_low = '|' + '_' * (max_width - 2) + '|'

figure = f'{horizontal_bound}\n{empty_slot}\n{two_pointers}\n{middle}\n{two_pointers}\n{empty_slot_low}'
print(figure)
