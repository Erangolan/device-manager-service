from flask import jsonify, make_response, request
from db import app
from Device import Device
import json


@app.route('/devices', methods=['GET'])
def devices():
    validDevices = []
    devices = Device.objects()
    for device in devices:
        if device.to_json() is not None:
            validDevices.append(device.to_json())

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
        )

        device.save()
        return {"msg": "added successfully to db!"}, 200
    return {"err": "already exist.."}, 404


@app.route("/devices/<id>", methods=['GET'])
def device(id):
    device = Device.objects(deviceId=id).first()
    if not device or device.to_json() is None:
        return jsonify({'err': 'doesnt exist'})

    return jsonify(device.to_json())


@app.route("/devices/<id>", methods=['PATCH'])
def updateDevice(id):
    updatedDev = json.loads(request.data)
    device = Device.objects(deviceId=id).first()

    if not device or device.to_json() is None:
        return {"err": "doesn't exist"}, 404

    device.update(
        airplane_id=device['airplane_id'] if updatedDev.get('airplane_id') is None else updatedDev.get('airplane_id'),
        serial_number=device['serial_number'] if updatedDev.get('serial_number') is None else updatedDev.get('serial_number'),
        description=device['description'] if updatedDev.get('description') is None else updatedDev.get('description')
    )

    return {"msg": "updated successfully!"}, 200


@app.route("/devices/<id>", methods=['DELETE'])
def deleteDevice(id):
    device = Device.objects(deviceId=id).first()

    if not device:
        return {"err": "doesn't exist"}, 404

    device.update(deleted=True)
    return {"msg": "deleted successfully!"}, 200


if __name__ == '__main__':
    app.run()
