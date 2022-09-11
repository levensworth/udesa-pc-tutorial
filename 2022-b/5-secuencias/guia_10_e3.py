

def nueva_tupla(tupla: tuple, indice: int, valor) -> tuple:
    lista = list(tupla)
    lista[indice] = valor
    return tuple(lista)

