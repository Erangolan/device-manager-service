from flask_mongoengine import MongoEngine
from flask import Flask
import os
from dotenv import load_dotenv
from pathlib import Path
dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': os.getenv('DB_HOST'),
    'username': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
}

db = MongoEngine()
db.init_app(app)
