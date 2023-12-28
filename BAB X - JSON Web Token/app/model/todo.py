from app import db
from datetime import datetime
from app.model.user import Users


class Todos(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    todo = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(
        db.BigInteger, db.ForeignKey(Users.id)
    )  # Relasi Many to One antar table users dengan todos
    users = db.relationship("Users", backref="user_id")

    def __repr__(self):
        return "<Todo {}>".format(self.todo)
