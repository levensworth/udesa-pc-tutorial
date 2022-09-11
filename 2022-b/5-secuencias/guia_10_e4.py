


def main():
    # pedir el string
    # trasnformo a mayuscula
    # mostrar el resultado
    
    string = get_string()
    new_str = transform_string(string)
    show_string(new_str)



def get_string() -> str:
    s = input('ingrese un string: ')
    return s


def show_string(s: str) -> None:
    print(s)


def transform_string(s: str) -> str:
    new_str = ''
    for c in s:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            distance = ord('a') - ord('A')
            new_str += chr(ord(c) - distance )

    return new_str