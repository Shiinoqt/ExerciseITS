from flask import Flask

# flask --app name run
# flask run --port --(if file is named app.py)


app = Flask(__name__)

@app.route("/")
def home() -> str:
    return "<h3>Hello, Flask!</h3>"

@app.route("/about")
def about() -> str:
    return "<h3>About Page</h3>"