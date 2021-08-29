import ujson
from bonsai_watering import devices, views

def get_devices():
    ''' bonsai_watering/status/devices '''
    return views.to_json(devices.devices)

def set_devices(message):
    '''
    bonsai_watering/set/devices
    expected json data -> {"name": "pump", "status": [01]}
    '''

    try:
        data = ujson.loads(message.decode('utf-8'))
        device = devices.get(data['name'])
        device.status = int(data['status'])
    except (TypeError, KeyError):
        print('Incorrect post data')
    except StopIteration:
        print('Incorrect device name')
    else:
        print('OK')
