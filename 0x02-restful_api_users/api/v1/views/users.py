#!/usr/bin/python3
""" users.py - users file """
from api.v1.views import app_views
from flask import jsonify, abort, request, make_response
from models.user import User
from models import db_session


@app_views.route("/users", methods=["GET", "POST"], strict_slashes=False)
def msgUsersListAll():
    """ msgUsersListAll() - return a List all Users or Create a User """
    r = []

    # List All Users
    # curl "http://0.0.0.0:5050/api/v1/users"
    if request.method == "GET":
        for user in db_session.query(User).all():
            print(user.to_dict())
            r.append(user.to_dict())
        return jsonify(r)

    # Create a User
    # curl -i -X POST -H 'Content-Type: application/json' -d '{
    # "first_name": "Felicia", "last_name": "Hsieh", "email": "123@abc.com",
    # "password": "123"}' http://0.0.0.0:5050/api/v1/users
    if request.method == "POST":
        u = User()
        u.first_name = "felicia"
        u.last_name = "hsieh"
        u.email = "123@abc.com"
        u.password = "mypass"
        db_session.add(u)
        db_session.commit()
        return jsonify(u.to_dict()), 201


@app_views.route("/users/<user_id>", methods=["GET", "DELETE", "PUT"],
                 strict_slashes=False)
def msgUsersSingleEntry(user_id):
    """ msgUsersSingleEntry() - modify a single user accordingly """
    print("****** IN SECOND USER FUNCTION: {} *****".format(user_id))

    u = User.get(user_id)
    if u is None:
        abort(404)

    # Get one User
    if request.method == "GET":
        return jsonify(u.to_dict())

    # Delete one User
    # curl -X DELETE http://0.0.0.0:5050/api/v1/users/[user_id]
    if request.method == "DELETE":
        db_session.delete(u)
        db_session.commit()

    # Update one User
    # curl -i -X PUT -H 'Content-Type: application/json' -d
    # '{"first_name": "Santa", "last_name": "Claus"}'
    # http://0.0.0.0:5050/api/v1/users/[user_id]
    if request.method == "PUT":
        print("***PUT REQUEST for {}***".format(user_id))

    if not request.json:
        return make_request(jsonify(error="Wrong format"), 400)
    if request.json.get('first_name'):
        u.first_name = request.json.get('first_name')
    if request.json.get('last_name'):
        u.last_name = request.json.get('last_name')
    db_session.commit()
    return jsonify(u.to_dict())
