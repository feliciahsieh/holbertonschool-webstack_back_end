#!/usr/bin/python3
""" app.py """
from flask import Flask
from api.v1.views import app_views
import os
from flask import render_template


app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def page_not_found(e):
    """ page_not_found() - handle 404 error """
    return jsonify({"error": "Not found"})


if __name__ == "__main__":
    envHost = os.environ.get('HBNB_API_HOST')
    envPort = int(os.environ.get('HBNB_API_PORT'))
    app.run(host=envHost, port=envPort)
