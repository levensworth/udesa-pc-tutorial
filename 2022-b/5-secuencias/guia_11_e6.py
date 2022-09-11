
'''
1.Implemente una función que solicite por consola el ingreso de una cadena que represente
una matriz y devuelva una lista de listas que la represente (cuyos elementos sean float).
Para ingresar cada matriz siga el siguiente ejemplo (las columnas se separan con espacios
y las filas con comas):



2.Defina una función que reciba dos matrices de 2x2, A y B. La función debe devolver una
matriz C igual a la suma matricial C=A+B. Luego implemente un programa que solicite las
matrices A y B por consola y devuelva C. 
'''

# tomamos esta funcion del ejercicio anterior
def create_vector(str_vec: str) -> tuple:
    return tuple([float(e) for e in str_vec.split()])

# ============ parte 1 =====================
def create_matrix(str_matrix: str) -> list:
    matrix = []
    for vec_str in str_matrix.split(','):
        matrix.append(list(create_vector(vec_str)))

    return matrix


def get_user_matrix() -> list:
    user_input = input('ingrese una matriz separando filas por comas (,): ')

    return create_matrix(user_input)


# ============ parte 2 =====================

def sum_matrix(m1: list, m2: list) -> list:
    
    # sanity check
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        # estamos chequeando que las matrices sean de igual dim.
        # esto no es un metodo exaustivo dado que estoy asumiendo 
        # que las matrices no son vacías y tienen todas sus sub-listas del mismo tamaño
        raise ValueError

    
    result = []
    
    for row_i in range(len(m1)):
        new_col = []
        for col_j in range(len(m2)):
            new_col.append(m1[row_i][col_j] + m2[row_i][col_j])

        result.append(new_col)
    
    return result


# Aux pero util

def show_matrix(matrix: list) -> None:
    '''
    Muestra una matriz por consola, utilizando un formato standard.

    args:
    matrix: (list of list) representa una matriz a mostrar.
    '''
    
    repr = '[\n'
    for row in matrix:
        str_row = [str(elem) for elem in row]
        repr += '\t'
        repr += ' '.join(str_row)
        repr += '\n'
    
    repr += ']'
    
    print(repr)


def main():
    m1 = get_user_matrix()

    m2 = get_user_matrix()

    m3 = sum_matrix(m1, m2)
    show_matrix(m3)


if __name__ == '__main__':
    main()
    
    

    
    
        





