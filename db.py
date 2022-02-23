from flask_mongoengine import MongoEngine
from flask import Flask
import os
from dotenv import load_dotenv
from pathlib import Path
dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': os.getenv('DB_NAME'),
    'host': os.getenv('DB_HOST'),
    'username': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'port': 5000
}
db = MongoEngine()
db.init_app(app)


class Device(db.Document):
    deviceId = db.StringField(unique=True)
    airplane_id = db.StringField()
    serial_number = db.StringField()
    description = db.StringField()
    deleted = db.StringField()

    def to_json(self):
        return {
            "deviceId": self.deviceId,
            "airplane_id": self.airplane_id,
            "serial_number": self.serial_number,
            "description": self.description,
            "deleted": self.deleted,
        }