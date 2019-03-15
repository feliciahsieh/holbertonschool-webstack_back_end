#!/usr/bin/python3
""" 1-warmup_flask.py - start a flask app with new route """

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """ index() - creates index.html
    Arguments: N/A
    Returns: N/A
    """
    return "Holberton School"

@app.route('/c', strict_slashes=False)
def messageC():
    """ messageC() - creates index.html
    Arguments: N/A
    Returns: N/A
    """
    return "C is fun!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
