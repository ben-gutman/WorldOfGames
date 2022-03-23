from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    try:
        file = open("Scores.txt", "r")
        current_score = file.read()
        app = Flask(__name__)
        return f'<html><head><title>Scores Game</title></head><body><h1>The score is <div id="score">{current_score}</div></h1></body></html>'
    except:
        return f'<<html><head><title>Scores Game</title></head><body><body><h1><div id="score" style="color:red">{"ERROR"}</div></h1></body></html>'
    finally:
        file.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port=5001)