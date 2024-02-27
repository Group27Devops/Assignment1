"""Module providing a function of app name"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Function printing Hello world."""
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
