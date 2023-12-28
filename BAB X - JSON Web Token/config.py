import os

class Config(object):
    # Mengambil nilai koneksi database dari file .flaskenv
    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))

    # Konfigurasi SQLALCHEMY (ORM) 
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    # Jwt secret key dari file .flaskenv
    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))