from Live import load_game, welcome
from Score import reset_score
from Utils import Screen_cleaner
import MainScores
import os

# Initializing the game
# reset_score()
Screen_cleaner()


os.system("start /b python MainScores.py")
welcome("Guy")
load_game()
