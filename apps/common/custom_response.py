from datetime import datetime

SUCCESS = 'success'
ERROR = 'error'


def success(data):
    return {'status': SUCCESS, 'data': data, 'time': datetime.now()}


def error(data):
    return {'status': ERROR, 'data': data, 'time': datetime.now()}
