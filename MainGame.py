from Live import load_game, welcome
from Score import reset_score
from Utils import Screen_cleaner
import MainScores

# Initializing the game
# reset_score()
Screen_cleaner()

welcome("Guy")
load_game()
MainScores.start()