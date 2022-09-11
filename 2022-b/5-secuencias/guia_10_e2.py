

def main():
    # obtener un string del usuario
    # invertirlo
    # mostrarlo


    string = get_string()

    rev_string = reversed_string(string)

    show_string(rev_string)



def get_string() -> str:
    return input('ingrese un string: ')


def reversed_string(s: str) -> str:
    rev_string = ''
    
    for i in range(len(s)):
        rev_string += s[len(s) - 1 -i]
    
    return rev_string


def show_string(string: str) -> None:
    print(string)

    
