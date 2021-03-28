from flask import Flask, render_template

app = Flask(__name__)

# Based off of http://phaser.io/tutorials/getting-started-phaser3/
@app.route("/getting-started")
def getting_started():
    return render_template("getting_started.html")

# Based off of http://phaser.io/tutorials/making-your-first-phaser-3-game/
@app.route("/first-game")
def first_game():
    return render_template("first_game.html")

if __name__ == "__main__":
    app.run(debug=True)