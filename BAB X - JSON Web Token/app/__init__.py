from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Inisiasi Flask
app = Flask(__name__)

# Gunakan konfigurasi database dari file config.py
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Inisiasi JWTManager
jwt = JWTManager(app)

# Import Module routes dan models
from app import routes
from app.model import todo, user
