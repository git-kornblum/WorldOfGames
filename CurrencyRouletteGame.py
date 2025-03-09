import freecurrencyapi
from random import randrange

def get_money_interval(difficulty):
    # https://app.freecurrencyapi.com/dashboard
    api_key = 'fca_live_Gkb33qEt5GbD7OVFxKRyuDtmwIWbYcerpe4xp6br'

    client = freecurrencyapi.Client(api_key)

    #print(client.status())

    # result = client.currencies(currencies=['USD', 'ILS'])
    # print(result)

    result = client.latest(currencies=['USD', 'ILS'])
    #print(result)

    dollar = randrange(1, 100)
    shekel = dollar * result["data"]["ILS"]
    total_value = shekel - (5 - difficulty), shekel + (5 - difficulty)

    return {"dollar": dollar, "shekel": shekel, "total_value": total_value}


def get_guess_from_user(dollar):
    print(f'What is the equivalent of ${dollar} in NIS (shekels)?')
    while True:
        try:
            users_guess = float(input("Your guess is: "))
            return users_guess
        except ValueError:
            print("Enter a amount, like 10 or 12.50")


def play(difficulty):
    dict = get_money_interval(difficulty)
    user_guess = get_guess_from_user(dict["dollar"])

    if user_guess > dict["total_value"][0] and user_guess < dict["total_value"][1]:
        print(f'Your guess is in the range. The precise amount is {dict["shekel"]:.2f} and your guess is between {dict["total_value"][0]:.2f} and {dict["total_value"][1]:.2f}')
        return True
    else:
        print(f'Bummer The precise amount is {dict["shekel"]:.2f} and your guess had to be between {dict["total_value"][0]:.2f} and {dict["total_value"][1]:.2f}')
        return False

