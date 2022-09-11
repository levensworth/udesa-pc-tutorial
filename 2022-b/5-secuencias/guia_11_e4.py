
def sum_inline(operation: str) -> float:
    seq = operation.split('+')
    cast_seq = [float(n) for n in seq]
    return sum(cast_seq)

def main():
    user_input = input('ingrese una operación: ')
    value = sum_inline(user_input)
    print('El resultado es: ', value)


if __name__ == '__main__':
    main()
