# import aplikasi flask dari file __init__.py
from app import app

@app.route("/")
def index():
    return "Hello World"

