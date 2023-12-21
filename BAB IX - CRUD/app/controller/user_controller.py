from app.model.user import Users
from app import response, app, db
from flask import request


# Controller function untuk mengambil seluruh data user
def index():
    try:
        users = Users.query.all()
        data = multiTransform(users)
        return response.OK(data, "Berhasil mengambil data users")
    except Exception as e:
        return response.BAD_REQUEST(None, "Gagal mengambil data users")


# Controller function untuk mengambil sebuah data user berdasarkan id
def show(id):
    try:
        user = Users.query.filter_by(id=id).first()
        # jika tidak terdapat user dengan id yang di input, maka return response not found
        if not user:
            return response.NOT_FOUND(None, "Data user tidak ditemukan")

        data = transform(user)
        return response.OK(data, "Berhasil mengambil data user berdasarkan id")
    except Exception as e:
        return response.BAD_REQUEST(None, "Gagal mengambil data users berdasarkan id")


def store():
    try:
        name = request.json["name"]
        email = request.json["email"]
        password = request.json["password"]

        user = Users(name=name, email=email)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()

        return response.OK(None, "Berhasil membuat data user")

    except Exception as e:
        return response.BAD_REQUEST(None, "Gagal membuat data user")


def update(id):
    try:
        name = request.json["name"]
        email = request.json["email"]
        password = request.json["password"]

        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.NOT_FOUND(None, "user tidak ditemukan")

        user.email = email
        user.name = name
        user.hash_password(password)

        db.session.commit()

        return response.OK(None, "Berhasil update data user")

    except Exception as e:
        return response.BAD_REQUEST(None, "Gagal update data user")


def delete(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.NOT_FOUND(None, "user tidak ditemukan")

        db.session.delete(user)
        db.session.commit()
        return response.OK(None, "Berhasil hapus data user")
    except Exception as e:
        return response.BAD_REQUEST(None, "Gagal hapus data user")


# Helper function untuk mengubah data user dari bentuk tupple menjadi dictionar
def transform(user):
    data = {"id": user.id, "name": user.name, "email": user.email}
    return data


def multiTransform(users):
    array = []
    for user in users:
        array.append(transform(user))
    return array
