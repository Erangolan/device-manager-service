from flask import jsonify, make_response, request
from db import Device, app
import json


@app.route('/devices', methods=['GET'])
def devices():
    validDevices = []
    devices = Device.objects()
    for device in devices:
        if device['deleted'] == "False":
            validDevices.append(device)

    return make_response(jsonify(validDevices), 200)


@app.route("/devices", methods=['POST'])
def add():
    record = json.loads(request.data)
    dev = Device.objects(deviceId=record['deviceId']).first() \
          or Device.objects(serial_number=record['serial_number']).first()

    if dev is None:
        device = Device(
            deviceId=record['deviceId'],
            airplane_id=record['airplane_id'],
            serial_number=record['serial_number'],
            description=record['description'],
            deleted=record['deleted']
        )
        device.save()
        return {"msg": "added successfully to db!"}, 200
    return {"err": "already exist.."}, 404


@app.route("/devices/<id>", methods=['GET'])
def device(id):
    device = Device.objects(deviceId=id).first()
    if not device:
        return jsonify({'err': 'doesnt exist'})

    return jsonify(device.to_json())


if __name__ == '__main__':
    app.run()
