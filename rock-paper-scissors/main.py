# definimos las opciones validas como:
# r = piedra
# s = tijera
# p = papel

import random
WINING_SCORE = 3

def get_user_name() -> str:
    user_name = input('What should I call you? > ')    
    return user_name


def get_user_option() -> str:
    while True:
        user_choice = input('What is your choice? [p, r, s] > ').lower()
        if user_choice != 'p' and user_choice != 'r' and user_choice != 's':
            print('Wrong option: choose from [p, r, s]')
        else:
            break
    return user_choice


def get_computer_option() -> str:
    return random.choice(('p', 'r', 's'))



def compute_round_winner(user_1_option: str, user_2_option: str) -> str:
    
    if (user_1_option == 'r' and user_2_option == 's') or  (user_1_option == 'p' and user_2_option == 'r') or (user_1_option == 's' and user_2_option == 'p'):
        return user_1_option
    
    if (user_1_option == 'r' and user_2_option == 'p') or  (user_1_option == 'p' and user_2_option == 's') or (user_1_option == 's' and user_2_option == 'r'):
        return user_2_option

    if user_1_option == user_2_option:
        return None
    

def compute_round_winner_name(user_1_name: str, option_1: str,  user_2_name: str, option_2: str) -> str:
    winner_option  = compute_round_winner(option_1, option_2)
    if winner_option == option_1:
        return user_1_name
    if winner_option == option_2:
        return user_2_name
    return None


def is_winner(score_1, score_2) -> bool:
    if score_1 >= WINING_SCORE or score_2 >= WINING_SCORE:
        return True
    return False


def display_winner(winner_name: str) -> None:
    print(f'The winner is {winner_name}!')


def display_round(user_name: str, user_option: str, computer_name: str, computer_option: str) -> None:
    print(f'user choice: {user_option}')
    print(f'computer choice: {computer_option}')
    winner = compute_round_winner_name(user_name, user_option, computer_name, computer_option)
    if winner != None:
        print(f'the winner is: {winner}')
    else:
        print(f"You both choose {user_option}")


def display_instructions() -> None:
    print('''
    Welcome to our little game:
    You'll need to give us a name.
    ''')

def game():
    display_instructions()
    user_name = get_user_name()
    computer_name = 'computer'
    user_score = 0
    computer_score = 0
    round_idx = 1
    while not is_winner(user_score, computer_score):
        print('Round: {round}'.format(round=round_idx))
        round_idx += 1
        user_option = get_user_option()
        computer_option = get_computer_option()
        winner = compute_round_winner(user_option, computer_option)
        display_round(user_name, user_option,computer_name, computer_option)
        if winner == user_option:
            user_score += 1
        elif winner == computer_option:
            computer_score += 1
            

    display_name = user_name if user_score == WINING_SCORE else computer_name
    display_winner(winner_name=display_name)
        
# el uso de if __name__ == '__main__': es comun en python 
# esto indica al interprete que solo debe ejecutar el siguiente código 
# cuando este archivo sea ejecutado. Ya veremos más adelante que hay diferentes 
# formas de utilizar este mismo código.
if __name__ == '__main__':
    game()
