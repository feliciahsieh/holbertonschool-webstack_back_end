#!/usr/bin/python3
""" index.py - index file """
from api.v1.views import app_views
from flask import jsonify

@app_views.route("/status", strict_slashes=False)
def msgStatus():
    """msgStatus() - return status msg """
    return jsonify({"status":"OK"})
