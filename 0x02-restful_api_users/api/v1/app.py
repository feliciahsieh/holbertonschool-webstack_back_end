#!/usr/bin/python3
""" app.py """
from flask import Flask
from api.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)


if __name__ == "__main__":
    envHost = os.environ.get('HBNB_API_HOST')
    envPort = int(os.environ.get('HBNB_API_PORT'))
    app.run(host=envHost, port=envPort)
