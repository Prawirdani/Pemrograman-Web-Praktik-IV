# import aplikasi flask dari file __init__.py
from app import app
from app.controller import user_controller
from flask import request


@app.route("/")
def index():
    return "Hello World"


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        return user_controller.index()
    elif request.method == "POST":
        return user_controller.store()


@app.route("/users/<id>", methods=["GET", "PUT", "DELETE"])
def user_by_id(id):
    if request.method == "GET":
        return user_controller.show(id)
    elif request.method == "PUT":
        return user_controller.update(id)
    elif request.method == "DELETE":
        return user_controller.delete(id)
