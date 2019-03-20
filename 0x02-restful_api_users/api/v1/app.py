#!/usr/bin/python3
"""
app.py
"""
import os
from api.v1.views import app_views
<<<<<<< HEAD
from flask import Flask, jsonify, render_template

=======
from flask import Flask, jsonify
>>>>>>> 5159687f7faed990eacad0a1091b3f8a3e9927a3

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def page_not_found(e):
    """ page_not_found() - handle 404 error """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    envHost = os.environ.get('HBNB_API_HOST')
    envPort = int(os.environ.get('HBNB_API_PORT'))
    app.run(host=envHost, port=envPort)
