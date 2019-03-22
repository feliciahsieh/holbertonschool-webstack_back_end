#!/usr/bin/python3
""" users.py - users file """
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models.user import User
from models import db_session


@app_views.route("/users", methods=["GET", "POST"], strict_slashes=False)
def msgUsersListAll():
    """ msgUsersListAll() - return a List all Users or create a User """
    r = []

    # Get All Users
    if request.method == "GET":
        for user in db_session.query(User).all():
            print(user.to_dict())
            r.append(user.to_dict())
        return jsonify(r)

    # Create a User
    if request.method == "POST":
        u = User()
        u["first_name"] = "Felicia"
        u["last_name"] = "Hsieh"
        u["email"] = "214@holbertonschool.com"
        u["password"] = "123"
        db_session.add(u)
        db_session.commit()
        return jsonify(u.to_dict()), 201


@app_views.route("/users/<user_id>", methods=["GET", "DELETE", "PUT"],
                 strict_slashes=False)
def msgUsersSingleEntry(user_id):
    """ msgUsersSingleEntry() - modify a single user accordingly """
    u = User.get(user_id)
    if u is None:
        abort(404)

    # Get one User
    if request.method == "GET":
        return jsonify(u.to_dict())

    # Delete one User
    if request.method == "DELETE":
        db_session.delete(u)
        db_session.commit()

    if request.method == "PUT":
        pass
