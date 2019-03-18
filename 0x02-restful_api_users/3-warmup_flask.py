#!/usr/bin/python3
""" 3-warmup_flask.py - start a flask app with environment vars """

from flask import Flask, jsonify
import os

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


@app.route('/hbtn', strict_slashes=False)
def messageHBTN():
    """ messageHBTN() - creates hbtn text
    Arguments: N/A
    Returns: N/A
    """
    r = {
        "C": "C is fun",
        "Python": "is cool",
        "Sysadmin": "is hiring"
    }

    return jsonify(r)


if __name__ == "__main__":
    envHost = os.environ.get('HBNB_API_HOST')
    envPort = int(os.environ.get('HBNB_API_PORT'))
    app.run(host=envHost, port=envPort)
