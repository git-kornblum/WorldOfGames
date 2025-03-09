from random import randrange
import os
from time import sleep


def generate_sequence(difficutly):
    numbers_list = []
    for i in range(1, difficutly + 1):
        numbers_list.append(randrange(1, 101))

    return numbers_list


def get_list_from_user(difficulty):
    user_input_list = []
    print(f'Enter the {difficulty} number(s):')

    for i in range(1, difficulty + 1):
        value = int(input(f'{i}. '))
        user_input_list.append(value)

    return user_input_list


def is_list_equal(numbers_list, user_input_list):
    return numbers_list == user_input_list

def show_list(numbers_list):
    print (f'remember the following sequence: {numbers_list}')
    sleep(0.7)

    # This does not work in pycharm, but works from the console
    os.system('cls' if os.name == 'nt' else 'clear')


def play(difficulty):
    numbers_list = generate_sequence(difficulty)
    show_list(numbers_list)

    user_input_list = get_list_from_user(difficulty)
    win = is_list_equal(numbers_list, user_input_list)

    if win:
        print('Yeah, you guessed the correct sequence. You win!')
        return True
    else:
        print(f'Nah, the correct sequence was {numbers_list}. You entered {user_input_list} You lose!')
        return False



