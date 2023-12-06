from flask import Flask

# Inisiasi Flask
app = Flask(__name__)

# Import Module routes
from app import routes
