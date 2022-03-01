from flask import Flask
def score_server():
    try:
        file = open("Scores.txt", "r")
        current_score = file.read()
        app = Flask(__name__)


        @app.route("/")
        def Score():
            return f'<html><head><title>Scores Game</title></head><body><h1>The score is <div id="score">{current_score}</div></h1></body></html>'


        if __name__ == '__main__':
            app.run()
    except:
        app = Flask(__name__)


        @app.route("/")
        def Score():
            return f'<<html><head><title>Scores Game</title></head><body><body><h1><div id="score" style="color:red">{"ERROR"}</div></h1></body></html>'


        if __name__ == '__main__':
            app.run()
    finally:
        file.close()
