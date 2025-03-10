
def add_score(difficulty):
    score = 0
    try:
        FILE = open("scores.txt", "r")
        score = int(FILE.read())
        FILE.close()

    except FileNotFoundError:
        with open("./scores.txt", "w") as FILE:
            FILE.write("0")
            FILE.close()
            score = 0

    except Exception as e:
        print ("An exception occurred:", type(e).__name__)

    if score >= 0:

        POINTS_OF_WINNING = (difficulty * 3) + 5

        score = score + POINTS_OF_WINNING

        with open("./scores.txt", "w") as FILE:
            FILE.write(str(score))
            FILE.close()

def reset_score():
    with open("./scores.txt", "w") as FILE:
        FILE.write("0")
        FILE.close()
