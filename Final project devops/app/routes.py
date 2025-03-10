# Creating an API for adding and retrieving data

from flask import Blueprint, request, jsonify
from app.models import db, User, Post

routes = Blueprint("routes", __name__)

@routes.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "username": u.username, "email": u.email} for u in users])

@routes.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    new_user = User(username=data["username"], email=data["email"], password=data["password"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added"}), 201

@routes.route("/posts", methods=["POST"])
def add_post():
    data = request.get_json()
    new_post = Post(title=data["title"], content=data["content"], user_id=data["user_id"])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created"}), 201
