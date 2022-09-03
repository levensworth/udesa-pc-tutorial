'''
Una terna pitagorica es aquella que cumple:

a ^2 + b^2 = c^2
donde a < b < c, enteros.

Encontrar la unica terna pitagorica que cumple:

a + b + c = 1000

source: https://projecteuler.net/problem=9
'''


def is_pythagorean_triplet(a: int, b: int, c: int) -> bool:
    is_square = a**2 + b ** 2 == c**2
    are_sequence = a < b and b < c
    return is_square and are_sequence


def find_triplet(number: int):
    max_num = number
    for c in range(max_num):
        for b in range(c):
            a = number - c - b # esto me lo da la constrain de la suma
            is_triplet = is_pythagorean_triplet(a, b, c)
            if is_triplet:
                return a, b, c

    return None

print(find_triplet(1000))