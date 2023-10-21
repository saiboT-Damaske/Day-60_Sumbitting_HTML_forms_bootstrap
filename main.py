from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    return "tadaa"


if __name__ == "__main__":
    app.run(debug=True)
