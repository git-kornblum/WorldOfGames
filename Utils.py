import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

def Screen_cleaner():
    # This does not work in pycharm, but works from the console
    os.system('cls' if os.name == 'nt' else 'clear')


