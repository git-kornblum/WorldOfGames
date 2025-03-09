import MemoryGame, GuessGame, CurrencyRouletteGame
from Score import add_score

def welcome(name):
    print(f'Hello {name} and welcome to the World of Games(WoG).\n'
          'Here you can find many cool games to play.\n')


def load_game():
    game = 0
    result = None
    while game < 1 or game > 3:
        game = int(input('1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n'
                         '2. Guess Game - guess a number and see if you chose like the computer\n'
                         '3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n'
                         'Please choose a game to play: '))

    difficulty = 0
    while difficulty < 1 or difficulty > 5:
        difficulty = int(input('Please choose game difficulty from 1 to 5: '))

    if game == 1:
        result = MemoryGame.play(difficulty)
    elif game == 2:
        result = GuessGame.play(difficulty)
    elif game == 3:
        result = CurrencyRouletteGame.play(difficulty)
    else:
        print('Incorrect input')

    if result:
        add_score(difficulty)