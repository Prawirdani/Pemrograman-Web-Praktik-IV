from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# Sebuah class merepresentasikan sebuah tabel dalam database, nama tabel yang di migrate  
# -otomatis mengikuti nama class
# variabel yang ditulis didalam class adalah kolom/field.

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {}>".format(self.name)



