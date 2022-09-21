
def calculate_total(options: dict, key: str, amount: float) -> int:
    if not options.get(key, False):
        return -1 # significa que no existe

    return options[key] * amount


def get_user_input() -> tuple:
    user_input = input('ingrese el nombre de la fruta seguido  de la cantidad')
    return [user_input.split(), float(user_input.split()[1])]


def show(fruit: str, total: float) -> None:
    if total == -1 :
        print('No existe esa fruta')
    print(f'Por {fruit} pagaras: ${total}')    


def main():
    fruits = {
        'Durazno': 200,
        'Manza': 120,
        'Peras': 150,
        'Naranjas': 110,
    }    
    

    key, amount = get_user_input()
    total = calculate_total(fruits, key, amount)

    show(key, total)