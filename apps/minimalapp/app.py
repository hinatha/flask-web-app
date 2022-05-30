from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, world."


@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)
