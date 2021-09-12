import ujson

from bonsai_watering import devices, views, queue

def get_devices():
    ''' bonsai_watering/status/devices '''
    return views.to_json(devices.devices)

def set_devices(topic, message, response_topic):
    '''
    bonsai_watering/set/devices/<name>
    expected json data -> {"status": [01]}
    '''
    device_name = topic.decode('utf-8').split('/')[-1]
    try:
        raw_data = message.decode('utf-8')
        data = ujson.loads(raw_data)
        device = devices.get(device_name)
        device.status = int(data['status'])
    except (TypeError, KeyError):
        data = 'Incorrect data `{}`'.format(data)
    except ValueError:
        data = 'Incorrect data `{}`'.format(raw_data)
    else:
        data = views.to_json(device)

    queue.append(data=data, topic=response_topic)
