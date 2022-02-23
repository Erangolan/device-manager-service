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


@app.route("/devices/<id>", methods=['PATCH'])
def updateDevice(id):
    updatedDev = json.loads(request.data)
    device = Device.objects(deviceId=id).first()

    if not device:
        return {"err": "doesn't exist"}, 404

    device.update(
        airplane_id=updatedDev.get('airplane_id') if not None else device['airplane_id'],
        serial_number=updatedDev.get('serial_number') if not None else device['serial_number'],
        description=updatedDev.get('description') if not None else device['description']
    )

    return {"msg": "updated successfully!"}, 200


if __name__ == '__main__':
    app.run()
