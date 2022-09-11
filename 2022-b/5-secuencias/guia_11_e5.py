
def create_vector(str_vec: str) -> tuple:
    return tuple([float(e) for e in str_vec.split()])


def get_user_input() -> str:
    return input('ingrese un vector: ')


def sum_vec(vec_1: tuple, vec_2: tuple) -> tuple:
    if len(vec_1) != len(vec_2):
        raise ValueError # esto no es posible

    result = []

    for i in range(len(vec_1)):
        result.append(vec_1[i] + vec_2[i])

    return tuple(result)


def main():
    vec1 = create_vector(get_user_input())
    vec2 = create_vector(get_user_input())

    res = sum_vec(vec1, vec2)

    print(res)



if __name__ == '__main__':
    main()



