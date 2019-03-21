#!/usr/bin/python3
""" index.py - index file """
from api.v1.views import app_views
from flask import jsonify
from models.user import User


@app_views.route("/status", strict_slashes=False)
def msgStatus():
    """msgStatus() - return status msg """
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def msgStats():
    """msgStats() - return stats msg """
    r = {}
    r["users"] = User.count()
    return jsonify(r)
