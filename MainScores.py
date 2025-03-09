from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route("/")
def score_server():
    score = None
    error = None

    try:
        file = open("scores.txt", "r")
        score = int(file.read())
        file.close()
    except TypeError:
        error =  "Score file does not exists\n"

    except Exception as e:
        return "An exception occurred:", type(e).__name__

    if score >= 0:
        return render_template('score.html', SCORE=score)
    else:
        return render_template('error.html', ERROR=error)

@app.route("/")
def start():
    app.run(host='0.0.0.0', port=80, debug=True)


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=80, debug=True)
