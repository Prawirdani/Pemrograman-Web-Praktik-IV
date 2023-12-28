from app.model.todo import Todos
from flask import request, jsonify
from app import response, db
from app.controller import user_controller
from flask_jwt_extended import jwt_required

@jwt_required() # Decorator untuk menandakan bahwa fungsi ini hanya bisa diakses dengan access token
def index():
    try:
        id = request.args.get("user_id")
        todos = Todos.query.filter_by(user_id=id).all()
        data = multiTransform(todos)
        return response.OK(data, "Berhasil mengambil data todo")
    except Exception as e:
        return response.BAD_REQUEST(None, "Terjadi kesalahan")


def show(id):
    try:
        todo = Todos.query.filter_by(id=id).first()
        if not todo:
            return response.NOT_FOUND(None, "Todo tidak ditemukan")

        data = transform(todo)
        return response.OK(data, "Berhasil mengambil data todo berdasarkan id")
    except Exception as e:
        return response.BAD_REQUEST(None, "Terjadi kesalahan")


def store():
    try:
        todo = request.json["todo"]
        desc = request.json["desc"]
        user_id = request.json["user_id"]

        todoNew = Todos(user_id=user_id, todo=todo, description=desc)
        db.session.add(todoNew)
        db.session.commit()

        return response.OK(None, "Berhasil tambah todo")
    except Exception as e:
        return response.BAD_REQUEST(None, "Terjadi kesalahan")


def update(id):
    try:
        todo = request.json["todo"]
        desc = request.json["desc"]

        todoData = Todos.query.filter_by(id=id).first()
        if not todoData:
            return response.NOT_FOUND(None, "Todo tidak ditemukan")
        todoData.todo = todo
        todoData.description = desc
        db.session.commit()
        return response.OK(None, "Berhasil update todo")
    except Exception as e:
        return response.BAD_REQUEST(None, "Terjadi kesalahan")


def delete(id):
    try:
        todoData = Todos.query.filter_by(id=id).first()
        if not todoData:
            return response.NOT_FOUND(None, "Todo tidak ditemukan")

        db.session.delete(todoData)
        db.session.commit()
        return response.OK(None, "Berhasil hapus todo")
    except Exception as e:
        return response.BAD_REQUEST(None, "Terjadi kesalahan")


def transform(value):
    data = {
        "id": value.id,
        "todo": value.todo,
        "user_id": value.user_id,
        "description": value.description,
        "created_at": value.created_at,
        "updated_at": value.updated_at,
        "user": user_controller.transform(value.users),
    }
    return data


def multiTransform(values):
    array = []
    for todo in values:
        array.append(transform(todo))
    return array
