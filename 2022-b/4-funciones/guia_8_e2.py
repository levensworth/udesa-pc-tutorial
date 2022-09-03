
def desc_udc(number: int):
    abs_rep = abs(number)
    unidades = abs_rep % 10
    decenas = (abs_rep // 10) % 10
    centenas = (abs_rep // 100) % 10

    return unidades, decenas, centenas
        

