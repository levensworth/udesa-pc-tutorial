from typing import List, Set, Tuple
from copy import copy

# conceptualmente
'''
mapa: List[List[int]] = []

point =  Tuple[int, int]
'''
ROCK = 1
EMPTY = 0

def are_connected(mapa: List[List[int]], from_point: Tuple[int, int], to_point: Tuple[int, int]) -> bool:
    '''
    Esta funcion devuelve si existe un camino posible entre los puntos
    que se piden.
    Params:
        - mapa: lista de listas represetando una matriz de enteros.
        - from_point: tupla de (row, col) representando un punto en la matriz desde donde partir.
        - to_point: tupla de (row, col) representando un punto en la matriz a donde se quiere ir
    Returns:
        True si es existe el camino, False si no.
    '''
    return search_path(mapa, from_point, to_point, set())


def search_path(
        mapa: List[List[int]], 
        current_point: Tuple[int, int], 
        to_point: Tuple[int, int], 
        visited: Set
    ) -> bool:
    '''
    Dado una instancia de un mapa y 2 puntos efectivamente busca si existe el camino.
    Parmas:
    Params:
        - mapa: lista de listas represetando una matriz de enteros.
        - current_point: tupla de (row, col) representando un punto en la matriz desde donde partir.
        - to_point: tupla de (row, col) representando un punto en la matriz a donde se quiere ir
        - visited: es un set de puntos ya visitados.
    Returns:
        True si es existe el camino, False si no.
    
    '''
    if current_point == to_point:
        return True

    found = False
    for point in get_neighbours(mapa, current_point):
        if is_available(visited, mapa, point):
            visited.add(point)
            current_visited = copy(visited)
            found = search_path(mapa, point, to_point, current_visited)
        if found:
            break
    
    return found


def get_neighbours(mapa: List[List[int]], point: Tuple[int, int]) -> List[Tuple[int, int]]:
    '''
    Dado un mapa y un punto, retorna la lista de puntos en su vecindario.
    Parmas:
        - mapa: lista de listas representando una matrix
        - point: tuple de (row, col) representando un punto dentro del mapa.
    Returns: 
        Lista de points
    '''
    directions = {
        '0': [1, 0],
        '45': [1, -1],
        '90': [0, -1],
        '135': [-1, -1],
        '180': [-1, 0],
        '225': [-1, 1],
        '270': [0, 1],
        '315': [1, 1]
    }
    rows = len(mapa)
    cols = len(mapa[0])
    neighbours = []
    for deltas in directions.values():
        possible_neighbour = (point[0]+ deltas[0], point[1]+ deltas[1])
        if is_inside_map(rows, cols, possible_neighbour):
            neighbours.append(possible_neighbour)
    return neighbours


def is_inside_map(num_rows: int, num_cols: int, point: Tuple[int, int]) -> bool:
    '''
    Dado un punto y los limites del mapa determinar si el punto es válido.
    Params:
        - num_rows: int representa la cantidad de filas en la matriz
        - num_cols: int representa la cantidad de columnas en la matriz
        - point: tupla (row, col) que representa un punto en la matriz.
    Returns:
        True si esta adentro false si no
    '''
    if point[0] < 0 or point[0] >= num_rows:
        return False
    
    if point[1] < 0 or point[1] >= num_cols:
        return False
    return True


def is_available(visited, mapa, point):
    '''
    Dado un punto y un mapa, verficar si la posición esta vacía y es posible utiilizarla o no.
    Paras:
        - visited: set de puntos que ya fueron utilizados.
        - mapa: lista de listas representando una matriz
        - point: Tupla de (row, col) representando el punto en el mapa.
    Returns:
        True si es posible usarlo, False si no.
    '''
    if point in visited:
        return False
    
    if mapa[point[0]][point[1]] != EMPTY:
        return False

    return True


# Descomentar para ver el uso.

# mapa = [
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0]
# ]

# print(are_connected(mapa, (0,0), (3, 4)))