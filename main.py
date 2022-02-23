from db import app


@app.route('/devices', methods=['GET'])
def devices():
    return True


if __name__ == '__main__':
    app.run()
