from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/user/<username>")
def user_profile(username: str):
    return render_template("user.html", title="User Profile", username=username)

@app.route("/square/<int:number>")
def square(number: int):
    result = number * number
    return render_template("result.html", title="Square", operation="Square", value=number, result=result)

@app.route("/sum/<int:a>/<int:b>")
def sum_numbers(a: int, b: int):
    result = a + b
    return render_template("result.html", title="Sum", operation="Sum", value=f"{a} + {b}", result=result)
