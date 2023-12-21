from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inisiasi Flask
app = Flask(__name__)

# Gunakan konfigurasi database dari file config.py
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import Module routes dan models
from app import routes
from app.model import todo, user
