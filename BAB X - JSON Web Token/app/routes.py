# import aplikasi flask dari file __init__.py
from app import app
from app.controller import user_controller, todo_controller
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


@app.route("/login", methods=["POST"])
def login():
    return user_controller.login()


@app.route("/todos", methods=["GET", "POST"])
def todo():
    if request.method == "GET":
        return todo_controller.index()
    else:
        return todo_controller.store()


@app.route("/todos/<id>", methods=["GET", "POST", "PUT", "DELETE"])
def todo_by_id():
    if request.method == "GET":
        return todo_controller.show(id)
    elif request.method == "PUT":
        return todo_controller.update(id)
    elif request.method == "DELETE":
        return todo_controller.delete(id)
