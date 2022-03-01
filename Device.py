from db import db


class Device(db.Document):
    deviceId = db.StringField(unique=True)
    airplane_id = db.StringField()
    serial_number = db.StringField()
    description = db.StringField()
    deleted = db.BooleanField(default=False)

    def to_json(self):
        if not self.deleted:
            return {
                "deviceId": self.deviceId,
                "airplane_id": self.airplane_id,
                "serial_number": self.serial_number,
                "description": self.description,
            }
        return None
