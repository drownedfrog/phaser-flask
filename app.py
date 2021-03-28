from flask import Flask, render_template

app = Flask(__name__)

@app.route("/getting-started")
def getting_started():
    return render_template("getting_started.html")

if __name__ == "__main__":
    app.run(debug=True)