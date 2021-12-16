from bonsai_watering import devices, views, queue, controllers, models

def get_devices():
    ''' bonsai_watering/status/devices '''
    return devices.devices

def set_devices(topic, message, response_topic=None):
    '''
    bonsai_watering/set/devices/<name>
    expected json data -> {"status": [01]}
    '''
    device_name = controllers.get_argument(topic)
    try:
        raw_data, data = controllers.parse(message)
        device = devices.get(device_name)
        device.status = int(data['status'])
    except (TypeError, KeyError, ValueError):
        {'error': 'Incorrect data `{}`'.format(raw_data)}
        queue.append(data=views.to_json({'error': 'Incorrect data `{}`'.format(raw_data)}), topic='bonsai_watering/errors')
