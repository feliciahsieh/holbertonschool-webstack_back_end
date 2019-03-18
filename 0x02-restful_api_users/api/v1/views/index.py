#!/usr/bin/python3
""" index.py - index fil e """

from flask import jsonify

@app.route("/status", strict_slashes=False)
def msgStatus():
    """msgStatus - return status msg """
    return jsonify({"status":"OK"})
