#!/usr/bin/python3
""" 0-warmup_flask.py - start a flask app """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """index()- send text back on home page """
    return "Holberton School"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
