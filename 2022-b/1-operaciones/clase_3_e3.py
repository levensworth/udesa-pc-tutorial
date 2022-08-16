'''
Un instagramer que reseña restaurantes desea automatizar la calificación y el cálculo del
costo total incluyendo propina de cada cena mediante un script de python. El programa
debe pedir el ingreso del nombre del restaurante, el costo del menú, el porcentaje a dejar
de propina y la calificación: :(, :|, :), :D. Finalmente se debe imprimir en pantalla un
resumen con la descripción de los datos ingresados y el gasto total.
Para el cálculo del gasto total incluya redondeo al entero más cercano. Guardar el
programa en un archivo que se llame menu_rest.py.

'''

restaurant_name = input("Enter restaurant's name: ")
menu_price = float(input('Enter menu price: '))
calification_str = input("Enter calification [ :(, :|, :), :D ]>  ")

if calification_str == ':(':
    calification = 1
elif calification_str == ':|':
    calification = 2
elif calification_str == ':)':
    calification = 3
elif calification_str == ':D':
    calification = 4
else:
    print('Calification not found!')
    exit() # cierra el programa

spaces = 30
max_calification = 4
print(f"""
Summary:
{'*'*spaces}
place:{' '* (spaces - len('place'))}{restaurant_name}

menu:{' '* (spaces - len('menu'))}{menu_price}

calification:{' '* (spaces - len('calification'))}{calification} / {max_calification}

TOTAL:{' '* (spaces - len('TOTAL'))}{round(menu_price)}

""")




