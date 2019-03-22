#!/usr/bin/python3
""" users.py - users file """
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models.user import User
from models import db_session


@app_views.route("/users", strict_slashes=False)
def msgUsersListAll():
    """msgUsersListAll() - return a list of all users """
    print("msgUsersListAll")
    result = User.all()
    print(result)
    # return jsonify(result)
    return {}
