from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("test_contact_form_page.html")


@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["user"]
    password = request.form["pw"]
    return f"<h1> Name: {name}, Password: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
