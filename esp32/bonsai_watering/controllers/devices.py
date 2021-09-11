import ujson

from bonsai_watering import devices, views

def get_devices():
    ''' bonsai_watering/status/devices '''
    return views.to_json(devices.devices)

def set_devices(topic, message, response_topic):
    '''
    bonsai_watering/set/devices/<name>
    expected json data -> {"status": [01]}
    '''
    device_name = topic.split('/')[-1]
    try:
        data = ujson.loads(message.decode('utf-8'))
        device = devices.get(device_name)
        device.status = int(data['status'])
    except (TypeError, KeyError):
        queue.append(data='Incorrect data', topic=response_topic)
    else:
        queue.append(data=views.to_json(device), topic=response_topic)
