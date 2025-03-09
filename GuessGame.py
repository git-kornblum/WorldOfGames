import random

def generate_number(difficult):
    if difficult <= 1:
        return 1
    else:
        return random.randrange(1, difficult)


def get_guess_from_user(difficult):
    return int(input(f"Give me a number between 1 and {difficult}: "))

def compare_results(secret_number, input_number):
    print(f'{secret_number} - {input_number}')
    if secret_number == input_number:
        return True
    else:
        return False


def play(difficult):
    secret_number = generate_number(difficult)
    input_number = get_guess_from_user(difficult)
    win = compare_results(secret_number, input_number)

    if win:
        print('Yeah, you guessed the correct number. You win!')
        return True
    else:
        print(f'Nah, the correct number was {secret_number}. You lose!')
        return  False

