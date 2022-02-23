from flask import jsonify, make_response
from db import Device, app


@app.route('/devices', methods=['GET'])
def devices():
    validDevices = []
    devices = Device.objects()
    for device in devices:
        if device['deleted'] == "False":
            validDevices.append(device)

    return make_response(jsonify(validDevices), 200)


if __name__ == '__main__':
    app.run()
