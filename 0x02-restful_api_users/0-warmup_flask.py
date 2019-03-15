#!/usr/bin/python3
""" 0-warmup_flask.py - start a flask app """

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """ index() - creates index.html
    Arguments: N/A
    Returns: N/A
    """
    return "Holberton School"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.url_map.strict_slashes = False
