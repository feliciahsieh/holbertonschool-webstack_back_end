#!/usr/bin/python3
""" users.py - users file """
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models.user import User
from models import db_session


@app_views.route("/users", methods=["GET", "POST"], strict_slashes=False)
def msgUsersListAll():
    """ msgUsersListAll() - return a list of all users """
    r = []
    for user in db_session.query(User).all():
        print(user.to_dict())
        r.append(user.to_dict())
    return str(r)
    #return jsonify([user.to_dict() for user in result])
