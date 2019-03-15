#!/usr/bin/python3
""" 1-warmup_flask.py - start a flask app with new route """

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """ index() - creates index.html
    Arguments: N/A
    Returns: N/A
    """
    return "Holberton School"

@app.route('/c')
def messageC():
    """ index() - creates index.html
    Arguments: N/A
    Returns: N/A
    """
    return "C is fun!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.url_map.strict_slashes = False
